"""
Main module to run the comparison
"""
import src.parse_current_versions as pcv
import src.get_source as gs
import src.get_latest_compatible as tl


def main():
    current_versions = pcv.parse_requirements_txt()

    for package in current_versions:
        src_versions = gs.get_pypi_versions(package)

        print(f"Current: {package}-{current_versions[package]}")

        if current_versions[package] != src_versions[0]:

            # TODO Preserve the current requirements.txt

            new = tl.latest_compatible_pypi_version(
                package,
                current_versions[package],
                src_versions
            )
            print(f"{package} latest compatible version: {new}\n")
        else:
            print(f"{package} is already at latest version\n")


if __name__ == "__main__":
    main()
