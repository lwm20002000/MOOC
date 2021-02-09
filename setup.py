from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name="edhec_risk_kit",
    version="1.0.0",
    license="MIT",
    description="Risk Analysis tools",
    author="Keigo Nagai",
    url="https://github.com/zlatax/MOOC.git",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt')
)