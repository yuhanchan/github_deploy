# import m2 # Error: No module named m2
from submodule import m2 # Work, but must know where is top level, 
                         # beacause absolute import start from top level
print(__name__+" from module in subfolder")