from setuptools import setup, find_packages

setup(
    name="jerico",
    version="1.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "jerico=jerico.main:main",
        ],
    },
    install_requires=[
        "psutil",
    ],
    python_requires='>=3.10',
)
