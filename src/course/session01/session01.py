import sys

from src.utils.dataframe import DataFrame

if __name__ == '__main__':
    # argument: full_path_to/housing.csv
    file_name = sys.argv[1]

    dt = DataFrame()
    dt.read_data_from_file(file_name, ",")
    # print(dt.describe())
    # print(dt.columns_names())
    dt.plot("longitude", "latitude", "population", 15, 8, "median_house_value")
    print("\nmissing data:")
    print(dt.missing_data())

    # dt.plot_columns_correlation()
