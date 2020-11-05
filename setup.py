"""Setup for chance to shine."""

from setuptools import find_packages, setup

NAME = "MACE"
PACKAGES = find_packages(where="src/")
print(PACKAGES)

REQUIRED = [
    'scipy',
    'matplotlib',
    'numpy',
    'pandas',
    'seaborn',
    'scikit-learn',
    'setuptools']

setup(
    name='shine',
    version='0.1.0',
    packages=PACKAGES,
    package_dir={"": "src"},
    url='',
    license='',
    author='CDT',
    author_email='greenr10@cardiff.ac.uk',
    long_description=open('README.md').read(),
    install_requires=REQUIRED
)
