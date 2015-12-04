from setuptools import setup, find_packages

setup(
    name = 'fptools',
    version = '1.0',
    author = "Brian Lee",
    description = "Basic library of functional programming related tools.",
    long_description = (
        "A small library of tools intended for working with generators/infinite sequences. "
        "Some of these are similar to itertools, or underscore.js."
    ),
    license = "MIT",
    keywords = "functional programming lists loops generators",
    install_requires = [],
    packages = find_packages(),
)
