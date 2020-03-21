import matplotlib.pyplot as plt
import pandas
import pandas as pd
import seaborn as sb
from pandas._typing import FrameOrSeries


class DataFrame:
    """
    A class used to represent a data table as a DataFrame
    ...

    Attributes
    ----------
    data_frame : pandas.DataFrame
        data structure to store the data as a DataFrame table
    file_name : str
        path and name of the file with all the data

    Methods
    -------
    read_data_file(file_name: str, delimiter: str)
        Read a data file given the file <file-full-path> and the columns delimiter
    """
    data_frame = {}
    file_name = ""

    def __init__(self):
        """Empty constructor
        """
        pass

    def read_data_file(self, file_name: str, delimiter: str):

        """Read a data file given the columns delimiter

        Parameters
        ----------
        file_name : str
            The sound the animal makes (default is None)
        delimiter : str
            The delimiter to split the data into columns
        Raises
        ------
        NotImplementedError
            If the file cant be found or opened
            parameter.
        """

        try:
            self.data_frame = pd.read_csv(file_name, na_values=['no info', '.'], sep=delimiter)
            self.file_name = file_name
        except IOError:
            print("Error: can\'t find file or read data")

    def read_tsv_data_file(self, file_name: str):
        """Read a specific tsv (tabulation) data file

        Parameters
        ----------
        file_name : str
            The sound the animal makes (default is None)
        Raises
        ------
        NotImplementedError
            If the file cant be found or opened
            parameter.
        """
        try:
            self.data_frame = pd.read_csv(file_name, delimiter='\t', na_values=['no info', '.'], encoding='utf-8',
                                          low_memory=False)
            self.file_name = file_name
        except IOError:
            print("Error: can\'t find file or read data")

    def describe(self) -> pandas.core.frame.DataFrame:
        """Get the basic information about the DataFrame
        Returns
        -------
        tuple3
        a tuple about struct, data-format, and basi information
        """

        return self.data_frame.head(), \
               self.data_frame.describe(include='all'), \
               self.data_frame.info()

    def columns_names(self) -> []:
        """Get the basic information about the DataFrame
        Returns
        -------
        list
        a list with all column names
        """
        return list(self.data_frame.columns)

    def delete_column(self, column_name: str):
        """Delete a column from the DataFrame if the specific column exists
        Parameters
        ----------
        column_name : str
            the name of the column to be deleted

        """
        if self.data_frame[column_name]:
            del self.data_frame[column_name]

    def preprocess(self, empty_rows: bool, one_column_data_missed: bool):
        """Delete rows based on row data missing
        Parameters
        ----------
        empty_rows : bool
            if we want to delete all empty rows
        one_column_data_missed: bool
            if we want to delete all empty rows with al least one columns without data
        """

        # Will drop the rows only if all of the values in the row are missing
        if empty_rows:
            self.data_frame.dropna(how='all', inplace=True)
        # Will drop a feature that has some missing values.
        if one_column_data_missed:
            self.data_frame.dropna(axis=1, inplace=True)

        # df = self.data_frame.dropna(axis=0)

    def missing_data(self) -> FrameOrSeries:
        """Get the head table about missing data in the dataframe
        Returns
        -------
        FrameOrSeries
        a table with 5 rows about missing data info
        """
        total = self.data_frame.isnull().sum().sort_values(ascending=False)
        percent = (self.data_frame.isnull().sum() / self.data_frame.isnull().count()).sort_values(ascending=False)
        missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])

        return missing_data.head()

    def plot(self, x_label: str, y_label: str, column: str, x_size: int, y_size: int, leyend_label: str):
        """Plot the dataframe given the sepecific parameters
        Parameters
        ----------
        x_label : str
            name of the x edge
        y_label: str
            name of the y edge
        column: str
            name column we want
        x_size: int
            size of the x edge
        y_size: int
            size of the y edge
        leyend_label: str
            name of the leyend
        """
        plotter = self.data_frame.copy()
        plotter.plot(kind="scatter", x=x_label, y=y_label, alpha=0.4, s=plotter[column] / 100,
                     label=column, figsize=(x_size, y_size), c=leyend_label, cmap=plt.get_cmap("jet"),
                     colorbar=True)
        plt.show()

    def plot_table_correlation(self):
        """Plot the dataframe
        """
        corrm = self.data_frame.corr()
        print(corrm)
        a = sb.heatmap(corrm,
                       xticklabels=corrm.columns,
                       yticklabels=corrm.columns,
                       cmap='RdBu_r',
                       annot=True,
                       linewidth=1)

        plt.show()
