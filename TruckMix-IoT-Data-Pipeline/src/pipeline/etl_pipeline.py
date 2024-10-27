import pandas as pd
from transformation import DataCleaner
from transformation import DataTransformer
import sqlalchemy

class ETLPipeline:
    def __init__(self, source, destination, transform_func):
        self.source = source
        self.destination = destination
        self.transform_func = transform_func

    def extract(self):
        # Extract data from source
        data = pd.read_csv(self.source)
        return data

    def transform(self, data):
        # Transform data using the provided transform function
        transformed_data = self.transform_func(data)
        return transformed_data

    def load(self, data):
        # Load data into the destination
        engine = sqlalchemy.create_engine(self.destination)
        data.to_sql('transformed_data', con=engine, if_exists='replace', index=False)

    def run(self):
        # Run the ETL pipeline
        data = self.extract()
        transformed_data = self.transform(data)
        self.load(transformed_data)

# Example transform function
def example_transform(data):
    # Perform some data transformations
    data['new_column'] = data['existing_column'] * 2
    return data

if __name__ == "__main__":
    source = 'TruckMix-IoT-Data-Pipeline/Data'
    destination = 'sqlite:///path/to/destination.db'
    pipeline = ETLPipeline(source, destination, example_transform)
    pipeline.run()