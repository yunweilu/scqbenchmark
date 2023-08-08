"""
setup.py - a module to allow package installation
"""

from distutils.core import setup


NAME = "scqbenchmark"
VERSION = "0.1"
DEPENDENCIES = [
    "scqubits",
    "py-cpuinfo",
    "primme",
    "threadpoolctl",
    "tqdm",
    "pandas"
]
PY_MODULE = []
DESCRIPTION = "a package for scqubits benchmark"
AUTHOR = "Yunwei LU"
AUTHOR_EMAIL = "yunweilu2020@u.northwestern.edu"

setup(author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      install_requires=DEPENDENCIES,
      name=NAME,
      version=VERSION,
      py_modules=PY_MODULE
)