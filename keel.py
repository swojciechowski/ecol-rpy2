import os
import io
import re

import numpy as np
import pandas as pd

DATASETS_DIR = 'data'

def parse_keel_dat(dat_file):
    with open(dat_file, "r") as fp:
        data = fp.read()
        header, payload = data.split("@data\n")

    attributes = re.findall(
        r"@[Aa]ttribute (.*?)[ {](integer|real|.*)", header)
    output = re.findall(r"@[Oo]utput[s]? (.*)", header)

    dtype_map = {"integer": 'Int64', "real": 'Float64'}

    columns, types = zip(*attributes)
    types = [*map(lambda _: dtype_map.get(_, 'category'), types)]
    dtype = dict(zip(columns, types))

    data = pd.read_csv(io.StringIO(payload), names=columns, dtype=dtype, na_values=['<null>', '?'])

    if not output:  # if it was not found
        output = columns[-1]

    target = data[output]
    data.drop(labels=output, axis=1, inplace=True)

    return data, target

def find_datasets(storage=DATASETS_DIR):
    for root, dirs, files in os.walk(storage):
        for f_name in filter(lambda _: '.dat' in _, files):
            yield os.path.join(root, f_name)


if __name__ == '__main__':
    for f_dir in find_datasets():
        ds_cat, ds_name = f_dir.split('.')[0].split('/')[-2:]
        data, target = parse_keel_dat(f_dir)

        features = len(data.dtypes)
        numeric_features = len(data.select_dtypes(include=['int', 'float']).dtypes)

        if features - numeric_features != 0:
            continue

        if data.isnull().values.any():
            continue

        print(f_dir)
        continue

        print("Name", ds_name)
        print("Category", ds_cat)
        print("Missing data", data.isnull().values.any())
        print("Classes", len(np.unique(target)))
        print("Features", features)
        print("Numeric Features", numeric_features)
        print()
