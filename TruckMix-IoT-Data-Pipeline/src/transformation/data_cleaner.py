import pandas as pd
from scipy.stats import zscore

class DataCleaner:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def remove_duplicates(self):
        self.data = self.data.drop_duplicates()
        return self

    def fill_missing_values(self, strategy='mean'):
        if strategy == 'mean':
            self.data = self.data.fillna(self.data.mean())
        elif strategy == 'median':
            self.data = self.data.fillna(self.data.median())
        elif strategy == 'mode':
            self.data = self.data.fillna(self.data.mode().iloc[0])
        else:
            raise ValueError("Unsupported strategy. Use 'mean', 'median', or 'mode'.")
        return self

    def remove_outliers(self, z_thresh=3):
        self.data = self.data[(zscore(self.data.select_dtypes(include=['number'])) < z_thresh).all(axis=1)]
        return self

    def get_clean_data(self):
        return self.data

# Example usage:
# df = pd.read_csv('your_data.csv')
# cleaner = DataCleaner(df)
# clean_df = cleaner.remove_duplicates().fill_missing_values().remove_outliers().get_clean_data()