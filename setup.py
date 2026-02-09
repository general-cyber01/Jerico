from setuptools import setup, find_packages

setup(
    name="jerico",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "jerico=jerico.main:main"
        ]
    },
)

