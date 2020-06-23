#!/usr/bin/env python
from setuptools import find_packages, setup
from setuptools.command.develop import develop as DevelopCommand
from distutils import log
from distutils.command.build import build as BuildCommand
from distutils.core import Command
from subprocess import check_output
import os


def get_requirements(env):
    with open("requirements-{}.txt".format(env)) as fp:
        return [x.strip() for x in fp.read().split("\n") if not x.startswith("#")]


install_requires = get_requirements("base")
VERSION = "0.1.0"

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))


class BuildAssetsCommand(Command):

    def initialize_options(self):
        self.work_path = os.path.join(
            ROOT_PATH, "src/service_bus/static/service_bus")

    def finalize_options(self):
        return []

    def run(self):
        self._run_command(["yarn", "install", "--quiet"])
        self._run_command(["yarn", "run", "build", "--quiet"])

    def _run_command(self, cmd, env=None):
        cmd_str = " ".join(cmd)
        log.debug(f"running [{cmd_str}]")
        try:
            return check_output(cmd, cwd=self.work_path, env=env)
        except Exception:
            log.error(f"command failed [{cmd_str}] via [{self.work_path}]")
            raise


class SBDevelopCommand(DevelopCommand):
    def run(self):
        self.run_command("build_assets")
        DevelopCommand.run(self)


class SBBuildCommand(BuildCommand):
    def run(self):
        self.run_command("build_assets")
        BuildCommand.run(self)


cmdclass = {
    "develop": SBDevelopCommand,
    "build": SBBuildCommand,
    "build_assets": BuildAssetsCommand,
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
    }
)
