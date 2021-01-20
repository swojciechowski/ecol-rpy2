import pandas as pd

import rpy2.rinterface_lib.callbacks
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri, default_converter
from rpy2.robjects.conversion import localconverter, py2rpy
from rpy2.robjects.vectors import FactorVector

silent_cb = lambda _: None
rpy2.rinterface_lib.callbacks.consolewrite_print = silent_cb
rpy2.rinterface_lib.callbacks.consolewrite_warnerror = silent_cb

ECOL = importr("ECoL")

def _prepare_X_y(X, y):
    # TODO: accept both pandas and numpy
    with localconverter(default_converter + pandas2ri.converter):
        r_X = ro.conversion.py2rpy(pd.DataFrame(X))
        r_y = FactorVector(ro.conversion.py2rpy(pd.Series(y)))

    return r_X, r_y

def _measures_to_dict(m):
    return { k : m.rx2(k)[0] for k in m.names }

def complexity(X, y):
    measures = ECOL.complexity(*_prepare_X_y(X, y))
    return _measures_to_dict(measures)

def overlapping(X, y):
    measures = ECOL.overlapping(*_prepare_X_y(X, y))
    return _measures_to_dict(measures)

def neighborhood(X, y):
    measures = ECOL.neighborhood(*_prepare_X_y(X, y))
    return _measures_to_dict(measures)

def linearity(X, y):
    measures = ECOL.linearity(*_prepare_X_y(X, y))
    return _measures_to_dict(measures)

def dimensionality(X, y):
    measures = ECOL.dimensionality(*_prepare_X_y(X, y))
    return _measures_to_dict(measures)

def balance(X, y):
    measures = ECOL.balance(*_prepare_X_y(X, y))
    return _measures_to_dict(measures)

def network(X, y):
    measures = ECOL.network(*_prepare_X_y(X, y))
    return _measures_to_dict(measures)
