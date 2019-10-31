from setuptools import setup


setup(
    name="mypackage",
    version="0.0.1",
    packages=["mypackage"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "run=scripts.run.py",
        ]
    }
)