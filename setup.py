from setuptools import setup, find_packages

setup(
    name = "my_test_repo",
    author = "Peter O'Connor",
    author_email = "poconn4@gmail.com",
    version = 0,
    dependency_links = (),
    install_requires = ['numpy'],
    scripts = [],
    packages=find_packages(),
    )
