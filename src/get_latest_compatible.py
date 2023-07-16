"""
Test newer versions of a package to see if it breaks
any of the unit tests.
"""
from typing import List, Union
import pytest


def latest_compatible_pypi_version(
    package: str,
    version: str,
    src_versions: List,
    root_path: str = "."
) -> Union[str, None]:
    """
    Iteratively test all new packages against the unit
    tests to check for warnings/errors
    """
    for src_version in src_versions:
        print(f"Testing {package} version: {src_version}")
        if version == src_version:
            return None

        # TODO test with a docker container
        # this way the dependencies can be installed and tested fluently
        pytest_out_code = pytest.main([root_path, "--no-header", "-v"])

        if pytest_out_code == 0:
            return src_version
