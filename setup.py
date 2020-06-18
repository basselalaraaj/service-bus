#!/usr/bin/env python
from setuptools import find_packages, setup


def get_requirements(env):
    with open("requirements-{}.txt".format(env)) as fp:
        return [x.strip() for x in fp.read().split("\n") if not x.startswith("#")]


install_requires = get_requirements("base")
VERSION = "0.1.0"

setup(
    name="service_bus",
    version=VERSION,
    author="Bassel Al Araaj",
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.7",
    install_requires=install_requires,
    zip_safe=False,
    include_package_data=True,
)
