import csv


def read_csv_as_dict(filename):
    """
        Read a csv file as a dictionary
    """
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)


if __name__ == '__main__':
    read_csv_as_dict("/Users/jcaso/Documents/ia/saturdaysAI/assets/session01/housing.csv")
