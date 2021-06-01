from ecol import *
import pandas as pd

def main():
    from sklearn.datasets import load_iris

    X, y = load_iris(return_X_y=True)
    print(X.dtype)
    print(y.dtype)
    # X = iris['data']
    # y = iris['target']

    # c = complexity(X, y)
    # print(pd.Series(c))

    print("overlapping")
    c = overlapping(X, y)
    print(pd.Series(c))

    print("neighborhood")
    c = neighborhood(X, y)
    print(pd.Series(c))

    print("linearity")
    c = linearity(X, y)
    print(pd.Series(c))

    print("dimensionality")
    c = dimensionality(X, y)
    print(pd.Series(c))

    print("balance")
    c = balance(X, y)
    print(pd.Series(c))

    print("network")
    c = network(X, y)
    print(pd.Series(c))


if __name__ == '__main__':
    main()
