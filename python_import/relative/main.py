from . import m1
from .submodule import m1 # This is relative import, 
                          # meaning import from here->submodule import m1

# from submodule import m1 # This would give the same result, 
                           # but is absolute import, and works only 
                           # when submodule is a subdirectory from here, 
                           # which is true in this case
print(__name__)