import unittest

from src.utils.dataframe import DataFrame


class DataFrameTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def read_data_file_test(self):
        # TODO
        dt = DataFrame().read_data_file("/Users/jcaso/Documents/ia/saturdaysAI/src/test/resources/csv_example.csv", ",")
        # self.assertEqual(dt, True, "Incorrect values")

        # self.assertEqual(nutrient.InControlRange(), dt, "Incorrect values")
