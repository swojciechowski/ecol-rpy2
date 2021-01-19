import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri, numpy2ri
from rpy2.robjects.conversion import localconverter
from rpy2.robjects.vectors import FactorVector

from sklearn.datasets import load_iris

ecol = importr("ECoL")
iris = load_iris()
X = pd.DataFrame(iris['data'], columns=iris['feature_names'])
# y = pd.Series(iris['target_names'].take(iris['target']))
y = pd.Series(iris['target'])
# print(data)
# print(target)
# print(iris)
# exit()

with localconverter(ro.default_converter + pandas2ri.converter):
    r_X = ro.conversion.py2rpy(X)
    r_y = ro.conversion.py2rpy(y)

r_y = FactorVector(r_y)
#
# with localconverter(ro.default_converter + numpy2ri.converter):
#     r_y = ro.conversion.py2rpy(y)

print(type(r_X))
print(type(r_y))

cmp = ecol.complexity(r_X, r_y)
d = { key : cmp.rx2(key)[0] for key in cmp.names }
print(pd.Series(d))
