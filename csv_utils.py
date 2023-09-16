
import pandas as pd

class DataUtils:
    @staticmethod
    def load_csv_df(filename):
        df = pd.read_csv(filename, delimiter=';')
        return df
    

