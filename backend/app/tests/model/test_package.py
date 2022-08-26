from app.model.package import Constraint, Dependency, Package


def test_package_parsing(example_data):
    packages = Package.extract_packages_from_lines(example_data)
    assert len(packages)
