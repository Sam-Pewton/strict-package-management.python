"""
Test newer versions of a package to see if it breaks
any of the unit tests.
"""
import re
import subprocess
from typing import List, Union


def latest_compatible_pypi_version(
    package: str,
    version: str,
    src_versions: List,
    root_path: str = "."
) -> Union[str, None]:
    """
    Iteratively test all new packages against the unit
    tests to check for warnings/errors.

    The side effect of this procedure leaves the
    requirements.txt file with the new package updated.

    :param package: the package to update
    :type package: str
    :param version: the current version in use
    :type version: str
    :param src_versions: all available versions
    :type src_versions: List
    :param root_path: the path to the project root
    :type root_path:

    :returns: the latest integratable version
    :rtype: str
    """
    current = version
    for src_version in src_versions:

        with open("requirements.txt", 'r', encoding="utf-8") as file:
            data = file.read()
        with open("requirements.txt", 'w', encoding="utf-8") as file:
            data = re.sub(
                f"{package}=={current}",
                f"{package}=={src_version}",
                data
            )
            file.write(data)
        current = src_version

        print(f"Testing {package} version: {src_version}")
        if version == src_version:
            break

        bash_out = subprocess.check_output(['bash', 'run_container.sh'])
        test_res = re.split(r'[=]+', re.sub(r'\\n[\']', '', str(bash_out)))[-2]

        if "failed" not in test_res.lower():
            return src_version
    return None
