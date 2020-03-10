import sys

from src.utils.utils import DataFrame

if __name__ == '__main__':
    # argument: full_path_to/housing.csv
    file_name = sys.argv[1]

    dt = DataFrame()
    dt.read_csv(file_name)
    # print(dt.describe())
    # print(dt.columns_names())
    # dt.plot()
    print("\nmissing data:")
    print(dt.missing_data())

    dt.plot_columns_correlation()
