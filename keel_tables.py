import pandas as pd

from ecol import complexity
from keel import find_datasets, load_dataset, prepare_X_y

def main():
    table = []

    for dataset in find_datasets():
        print(dataset)
        X, y = load_dataset(dataset, return_X_y=True)
        table.append({
            "Dataset": dataset,
            **complexity(X, y)
        })

    df = pd.DataFrame(table)
    print(df.to_markdown())
    df.to_csv('keel_imbl_cmplx.csv')


if __name__ == '__main__':
    main()
