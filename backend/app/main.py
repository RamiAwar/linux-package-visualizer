import json
from collections import defaultdict
from typing import Dict, List

from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from app.config import settings
from app.model.package import Package

app = FastAPI()
packages: Dict[str, Package] = {}
graph: Dict[str, List[str]] = defaultdict(list)


@app.on_event("startup")
async def startup():
    global packages, graph

    # For simplicity, load all packages into memory
    # If we wanted to productionize this, we could use an sqlite database since I imagine this service
    # would be spawned on each container as a kind of monitoring attempt, so it shouldn't take up
    # too much memory so as not to affect other apps running on the same container
    package_list = Package.extract_packages_from_file(settings.package_file)

    # If this was a much bigger file, I would've used a generator to get the packages and process them in a pipeline
    for package in package_list:
        packages[package.name] = package

    # Inject reverse dependencies now that we have all the packages
    for package in package_list:
        # Search all other packages for dependencies
        # O(n^2) but only going to be built once so it's fine
        for other_package in package_list:
            if not other_package.depends:
                continue

            for dep in other_package.depends:
                if dep[0] == package.name:
                    package.reverse_depends.append((other_package.name, dep[1]))  # NOTE: This is a reverse constraint


@app.get("/all")
async def get_all_packages():
    return {"packages": list(packages.keys())}


@app.get("/package/{package_name}")
async def get_package(package_name: str):
    if packages.get(package_name):
        return packages[package_name].dict()

    return HTTPException(status_code=404, detail="Package not found")
