from setuptools import setup, find_packages

setup(
    name="cli-data-utility",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest",
    ],
    entry_points={
        'console_scripts': [
            'csv-cleaner=main:main',
        ],
    },
)