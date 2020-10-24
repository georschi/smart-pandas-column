
from setuptools import find_packages, setup
from glob import glob

name = 'smart-pandas-column'

setup(
    name='smart-pandas-column',
    packages=[p for p in find_packages() if p.startswith('smart')],
    version='0.1.1',
    description='Smart Pandas Column overloads pandas to provide fault tolerant column retrieval ',
    author='Georgios Schinas',
    author_email='georschi@outlook.com',
    license='',
    install_requires='pandas',
)