from distutils.core import setup
from cython.Build import cythonize

setup(
  name = 'Cython program',
  ext_modules = cythonize("cython_integrator.pyx"),
)
