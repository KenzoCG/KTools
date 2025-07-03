# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import inspect

# ------------------------------------------------------------------------------- #
# FUNCTIONS
# ------------------------------------------------------------------------------- #

def get_function_info(func):
    info = None
    try:
        func_name = func.__name__
        signature = str(inspect.signature(func))
        docstring = inspect.getdoc(func)
        info = {
            'FUNC' : func,
            'NAME' : func_name,
            'DEF'  : f"{func_name}{signature}",
            'DOC'  : docstring,
        }
    except: pass
    return info
