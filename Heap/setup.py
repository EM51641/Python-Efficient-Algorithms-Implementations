import cython
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="heapify",
    ext_modules=cythonize("Heapify.pyx", language_level=3)
)
