#!/usr/bin/env python
from setuptools import find_packages, setup
from setuptools.command.develop import develop as DevelopCommand


def get_requirements(env):
    with open("requirements-{}.txt".format(env)) as fp:
        return [x.strip() for x in fp.read().split("\n") if not x.startswith("#")]


install_requires = get_requirements("base")
VERSION = "0.1.0"


class DispatchDevelopCommand(DevelopCommand):
    def run(self):
        DevelopCommand.run(self)


cmdclass = {
    "develop": DispatchDevelopCommand,
}


setup(
    name="service_bus",
    version=VERSION,
    author="Bassel Al Araaj",
    author_email='info@bassel.dev',
    url='https://github.com/basselalaraaj/service-bus',
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
    cmdclass=cmdclass,
    zip_safe=False,
    include_package_data=True,
    entry_points={
        "console_scripts": ["service_bus = service_bus.cli:entrypoint"],
    },
)
