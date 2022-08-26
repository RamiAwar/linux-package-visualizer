from __future__ import annotations  # Needed to return class type from class method

from typing import Iterable, List, Optional, Tuple, Union

from pydantic import BaseModel, Field


class Dependency(BaseModel):
    """Dependency forms a node in the dependency graph"""

    name: str


class Constraint(BaseModel):
    """Version constraint is used to detect conflicts in the dependency graph."""

    # Why is this a model if it only has one field?
    # Because we might need to add functionality later, like parsing the version constraint.
    # This requires some logic to detect all different types of version constraints, etc.
    # Models serve to couple data and operations on that data in one place.
    version_constraint: str


class Package(BaseModel):
    name: str = Field(alias="package")
    status: str
    maintainer: str
    version: str
    description: str

    # Union here is a hack to allow for strings to be written temporarily to deps/alts and get parsed later, saves some memory
    depends: Optional[Union[List[Tuple[Dependency, Constraint]], str]]
    alts: Optional[Union[List[Tuple[Dependency, Constraint]], str]]
    conflicts: Optional[Union[List[Tuple[Dependency, Constraint]], str]]
    suggests: Optional[Union[List[str], str]]

    priority: Optional[str]
    section: Optional[str]
    installed_size: Optional[int]
    architecture: Optional[str]
    homepage: Optional[str]

    def parse_dependencies(self):
        """Parse dependency string into list of dependency constraint tuples"""
        if self.depends:
            depends_and_alts = self.depends.split(" | ")
            depends = depends_and_alts[0].split(", ")
            alts = depends_and_alts[1].split(", ") if len(depends_and_alts) > 1 else None

            if depends:
                for i, dep in enumerate(depends):
                    constraint = None
                    first_parenthesis = dep.find("(")
                    if first_parenthesis:
                        constraint = dep[first_parenthesis + 1 : dep.find(")")]
                        constraint = Constraint(version_constraint=constraint)

                    depends[i] = (dep[:first_parenthesis].strip(), constraint)

            # Not extracting this into a function since it will never be used anywhere else, not worth
            if alts:
                for i, dep in enumerate(alts):
                    constraint = None
                    first_parenthesis = dep.find("(")
                    if first_parenthesis:
                        constraint = dep[first_parenthesis + 1 : dep.find(")")]
                        constraint = Constraint(version_constraint=constraint)

                    alts[i] = (dep[:first_parenthesis].strip(), constraint)

            self.depends = depends
            self.alts = alts

    @classmethod
    def extract_packages_from_file(cls, filename: str) -> Iterable[Package]:
        """Extract packages from a file"""
        with open(filename) as f:
            return cls.extract_packages_from_lines(f.readlines())

    @classmethod
    def extract_packages_from_lines(cls, lines: Iterable[str]) -> List[Package]:
        """Extract packages from a file"""
        current_package = {}
        packages = []
        description_parsing = False  # Flag for multiline description parsing

        for line in lines:
            line = line.strip()

            if line == "":
                # Parse package and move to next
                if current_package:
                    package = Package(**current_package)
                    package.parse_dependencies()
                    packages.append(package)

                current_package = {}
                continue

            try:
                key, value = line.split(": ", 1)  # Ensure only first colon is used
            except ValueError:
                if description_parsing:
                    current_package["description"] = current_package["description"] + f"\n{line}"
                    continue

            description_parsing = key == "Description"
            current_package[key.lower()] = value.strip()
