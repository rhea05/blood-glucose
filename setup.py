# Shohini's setup file
from setuptools import setup, find_packages

setup(
    name="mdp",
    version="0.1",
    packages=['mdp'],
    install_requires=['gym==0.9.4'],
    include_package_data=True
)


