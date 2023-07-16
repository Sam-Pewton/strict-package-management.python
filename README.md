# strict-package-management.python

Automatically manage packages whilst retaining a strict list of dependencies. Leverage the unit tests in your projects to determine if a new package version will break your service.

## Requirements
- Docker
- Docker buildx
- Python 3.7 or greater
- requests, packaging, and pytest libraries installed

## Usage
For now, this repository will only update its own files locally.

To run:
- Clone the repository
- Set the packages in the requirements.txt file. To see them update, be sure to set them lower than the latest versions available.
- In the terminal, run `python version_updater.py`.
