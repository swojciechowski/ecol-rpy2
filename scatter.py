import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.neighbors import KernelDensity
from sklearn.utils.fixes import parse_version


def main():
    df = pd.read_csv('complexity.csv', index_col=0)
    df = df.transpose()

    cols = [c for c in df.columns if 'sd' not in c.lower()]
    df=df[cols]

    columns = df.columns.to_list()
    print(columns)

    X = df.values
    n_objects, n_features = X.shape
    print(n_objects, n_features)

    fig, ax = plt.subplots(n_features, n_features, figsize=(60, 60))

    for i in range(n_features):
        for j in range(n_features):
            if i < j:
                continue
            print(i, j)
            ax[i, j].scatter(X[:, i], X[:, j], s=10, alpha=0.8)
            ax[i, j].set_title(f"{columns[i]} \n {columns[j]}")

    plt.tight_layout()
    plt.savefig("foo.png")

if __name__ == '__main__':
    main()
