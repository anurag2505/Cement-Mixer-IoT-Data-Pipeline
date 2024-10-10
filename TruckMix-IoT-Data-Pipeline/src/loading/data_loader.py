import pandas as pd
import json

class DataLoader:
    def __init__(self, source):
        self.source = source

    def load_data(self):
        """
        Load data from the source.
        This method should be implemented to load data from the specified source.
        """
        raise NotImplementedError("This method needs to be implemented by subclasses.")

class CSVDataLoader(DataLoader):
    def load_data(self):
        try:
            data = pd.read_csv(self.source)
            return data
        except Exception as e:
            print(f"Error loading data from {self.source}: {e}")
            return None

class JSONDataLoader(DataLoader):
    def load_data(self):
        try:
            with open(self.source, 'r') as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(f"Error loading data from {self.source}: {e}")
            return None

# Example usage:
# csv_loader = CSVDataLoader('path/to/csvfile.csv')
# data = csv_loader.load_data()
# print(data)