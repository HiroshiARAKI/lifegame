import os
from setuptools import setup, find_packages


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


setup(
    name='LifeGame',
    version='0.3.0',
    description='Simple Conway\'s Game of Life Simulator on Python',
    long_description='README.md',
    author='Hiroshi ARAKI',
    author_email='araki@hirlab.net',
    install_requires=read_requirements(),
    url='https://github.com/HiroshiARAKI/lifegame',
    license='MIT',
    packages=find_packages(exclude=('examples', 'save', 'tests')),
    test_suite='tests',
)
