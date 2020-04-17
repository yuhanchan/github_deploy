from ..submodule2 import m2
# import m11 # Error: no mocule named m11
from . import m11 # Work
print(__name__+" from submodule")