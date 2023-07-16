"""
Main module to run the comparison
"""
import os
import shutil
import src.parse_current_versions as pcv
import src.get_source as gs
import src.get_latest_compatible as tl


def main():
    current_versions = pcv.parse_requirements_txt()
    shutil.copy("./requirements.txt", "./requirements.bak")
    
    for package in current_versions:
        src_versions = gs.get_pypi_versions(package)

        print(f"Current: {package}-{current_versions[package]}")

        if current_versions[package] != src_versions[0]:

            shutil.copy("./requirements.txt", "./requirements.txt.old")

            new = tl.latest_compatible_pypi_version(
                package,
                current_versions[package],
                src_versions
            )

            if new:
                print(f"{package} latest compatible version: {new}\n")
            else:
                print(f"no new versions are compatible for {package}.")
                shutil.copy("./requirements.txt.old", "./requirements.txt")

            os.remove("./requirements.txt.old")
        else:
            print(f"{package} is already at latest version\n")


if __name__ == "__main__":
    main()