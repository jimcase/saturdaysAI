import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb


class DataFrame:
    data_frame = {}
    file_name = ""

    def __init__(self):
        pass

    def read_data_file(self, file_name, delimiter):

        try:
            self.data_frame = pd.read_csv(file_name, na_values=['no info', '.'], sep=delimiter)
            self.file_name = file_name
        except IOError:
            print("Error: can\'t find file or read data")

    def describe(self):
        return self.data_frame.head(), \
               self.data_frame.describe(include='all'), \
               self.data_frame.info()

    def columns_names(self):
        return list(self.data_frame.columns)

    def delete_column(self, column_name):
        if self.data_frame[column_name]:
            del self.data_frame[column_name]

    def preprocess(self):
        # Will drop the rows only if all of the values in the row are missing
        self.data_frame.dropna(how='all', inplace=True)
        # Will drop a feature that has some missing values.
        self.data_frame.dropna(axis=1, inplace=True)
        # df = self.data_frame.dropna(axis=0)

    def missing_data(self):

        total = self.data_frame.isnull().sum().sort_values(ascending=False)
        percent = (self.data_frame.isnull().sum() / self.data_frame.isnull().count()).sort_values(ascending=False)
        missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])

        return missing_data.head()

    def plot(self, x_label, y_label, column, x_size, y_size, leyend_label):
        plotter = self.data_frame.copy()
        plotter.plot(kind="scatter", x=x_label, y=y_label, alpha=0.4, s=plotter[column] / 100,
                     label=column, figsize=(x_size, y_size), c=leyend_label, cmap=plt.get_cmap("jet"),
                     colorbar=True)
        plt.show()

    def plot_table_correlation(self):
        corrm = self.data_frame.corr()
        print(corrm)
        a = sb.heatmap(corrm,
                       xticklabels=corrm.columns,
                       yticklabels=corrm.columns,
                       cmap='RdBu_r',
                       annot=True,
                       linewidth=1)

        # a.invert_yaxis()
        # a.xaxis.tick_top()
        plt.show()
