import pandas as pd
from datetime import datetime

def add_metadata(data: pd.DataFrame, source: str, version: str) -> pd.DataFrame:
    """
    Adds metadata to the DataFrame.

    Parameters:
    data (pd.DataFrame): The input data.
    source (str): The source of the data.
    version (str): The version of the data.

    Returns:
    pd.DataFrame: The data with added metadata.
    """
    metadata = {
        'source': source,
        'version': version,
        'timestamp': datetime.utcnow().isoformat()
    }
    
    for key, value in metadata.items():
        data[key] = value
    
    return data

# Example usage
if __name__ == "__main__":
    # Sample data
    df = pd.DataFrame({
        'sensor_id': [1, 2, 3],
        'value': [10, 20, 30]
    })
    
    enriched_df = add_metadata(df, source="IoT Sensor", version="1.0")
    print(enriched_df)