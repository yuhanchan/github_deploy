## This folder test python import (absolute import vs. relative import)

---

### Some concepts to understand beforehand:
- Note that all the discussion about absolute and relative import is only applicable to **in package** import (the import statements in files that in a folder with `__init__.py`)
- Package: A folder containing a `__init__.py` file is a package. (`__init__.py` could be empty)
- Top level module: If you run a python script, then the level the script is in is the top level. `__name__` for this module will be `__main__`
    - For example, in this folder, you can run `python top.py`, will output `__main__`
- python 2.x uses defaults to **relative import**, python 3.x defaults to **absolute import**
- Top level has no relative path (I guess because you can not go above top level (parent level), so it make no sense to have relative import. Since you can only go down, you should always use absolute import on top level.)


---

In absolute 
python import search for:
- Current path
- `PYTHONPATH` env viriable
- Python lib

absolute import looks sth like `import A` or `from A import B`

absolute import can import modules from its own folder, and its subfolders, but **NOT** from its parent folders.
- For example, in absolute/main.py, we can import module `m1` and `submodule.m1`, but not `top`.


---

relative import looks sth like `from . import A` or `import ..B`, where `.` is the current module, and `..` is the last level module, etc

relative import must have package structure, and can only import moudle **inside/beneath/under** the top level, so:
- **CANNOT** run `python main.py` in `relative/` folder
- **CAN** run `python -m relative.main` from `python_import/` folder, which is a level higher than `relative`.
- relative import is usually useful when need to import from a non-submodule or from the same foler, for example, in `relative/submodule/m1.py`, it imported `relative/submodule/m2.py`, which cannot be done by absolute import (unless add the path to $PYTHONPATH)
- Overall, **NEVER** use relative import on top level, that is, in the script you run directly.

---

Insight:
- relative `.`, `..` means relative **to the file itself**, not to where the toplevel is ran. absolute always start path from top level.
- Use absolute import on top level, and use relative import in lower level (packages).
- Interestingly, relative import was strongly discouraged back in 2010, I guess because it's not very readable. But it's no longer strongly discouraged, I still find it stupid that in absolute import you need to 'go back to the top' every time you try to import sth, especially when it's right in the current folder... https://stackoverflow.com/questions/4209641/absolute-vs-explicit-relative-import-of-python-module