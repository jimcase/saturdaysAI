from src.utils.dataframe import DataFrame


class Utils:

    def __init__(self):
        pass

    @staticmethod
    def to_csv(data_frame: DataFrame):
        return data_frame.to_csv()

    @staticmethod
    def to_json(data_frame: DataFrame):
        return data_frame.to_json()
