import os
import io
import re
from setuptools import setup


def read(*names, **kwargs):
    """Read a file and return its content, skip all errors."""
    try:
        with io.open(
                os.path.join(os.path.dirname(__file__), *names),
                encoding=kwargs.get("encoding", "utf8")
        ) as fp:
            return fp.read()
    except IOError:
        return ''


def find_version(*file_paths):
    """Find the version number in a given file."""
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="mypackage",
    version=find_version("tsgsim", "__init__.py"),
    packages=["mypackage"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "run=scripts.run.py",
        ]
    }
)