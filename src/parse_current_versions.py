"""
Parse the current requirements for a repository
"""
import re
from typing import Dict


def parse_requirements_txt(file_path: str = "../requirements.txt") -> Dict:
    """
    Parse a requriements.txt file.

    :param file_path: the path to the requirements file
        defaults to '../requirements.txt'
    :type file_path: str

    :returns: the parsed requirements
    :rtype: Dict
    """
    with open(file_path, 'r', encoding="utf-8") as file:
        pkgs = [re.sub(r'\n', '', data) for data in file.readlines()]

    full_requirements = {
        re.split(r"==", package)[0]: re.split(r"==", package)[1]
        for package in pkgs
    }
    return full_requirements


if __name__ == "__main__":
    print(parse_requirements_txt())
