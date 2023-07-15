"""
Module to retrieve a list of all versions for a specific package

TODO split by major versions in a dict.
"""
import requests
from packaging import version
from typing import List


def get_pypi_versions(package_name: str) -> List:
    """
    Get a list of all versions available for a package on PyPI

    The latest version is indexed first in the list.

    :param package_name: the name of the package to search for
    :type package_name: str

    :returns: an ordered list of all versions available for a package
    :rtype: List
    """
    r = requests.get(
            f'https://pypi.org/pypi/{package_name}/json',
            headers={'Accept': 'application/json'}
        )
    versions = list(r.json()["releases"].keys())
    versions = sorted(versions, key=lambda x: version.Version(x), reverse=True)
    return versions


def get_conda_forge_versions(package_name: str) -> None:
    pass


if __name__ == "__main__":
    print(get_pypi_versions("pika"))
    print(get_pypi_versions("pydantic"))
    print(get_pypi_versions("numpy"))
    print(get_pypi_versions("pandas"))
    print(get_pypi_versions("requests"))
    print(get_pypi_versions("pytest"))
