import os

import setuptools


def _read_reqs(path):
    full_path = os.path.join(os.path.dirname(__file__), path)
    with open(full_path) as f:
        return [
            s.strip() for s in f.readlines() if (s.strip() and not s.startswith("#"))
        ]


setuptools.setup(
    name="ads_manager",
    version="1.0.0",
    author="ndinevski",
    install_requires=_read_reqs("requirements.txt"),
    packages=setuptools.find_packages(),
    include_package_data=True,
)
