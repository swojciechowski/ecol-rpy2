import numpy as np
import pandas as pd

from keel import parse_keel_dat
from ecol import complexity
from sklearn.preprocessing import LabelEncoder

CONFIG_FILE = 'data/config.txt'
RESULTS_FILE = 'results.csv'

def find_datasets():
    with open(CONFIG_FILE, 'r') as fp:
        for line in fp.readlines():
            yield line.strip()

def main():
    results = {}
    for ds_file in find_datasets():
        ds_name = ds_file.strip().split('/')[-1].split('.')[0]
        print(ds_name)

        data, target = parse_keel_dat(ds_file)
        X = data.to_numpy(dtype=np.float)
        y = target.to_numpy().ravel()
        y = LabelEncoder().fit_transform(y)

        results[ds_name] = complexity(X, y)

    df = pd.DataFrame(results).transpose()
    df.to_csv(RESULTS_FILE)


if __name__ == '__main__':
    main()
