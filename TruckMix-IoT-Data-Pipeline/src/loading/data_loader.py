
import pandas as pd
import os

def load_csv_files():
    """
    Reads 5 CSV files from the Data folder
    Returns a list of DataFrames containing the data from each CSV file
    """
    data_folder = "TruckMix-IoT-Data-Pipeline/Data"
    dataframes = []
    
    try:
        # Get list of CSV files in the Data folder
        csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]
        
        # Read first 5 CSV files
        for file in csv_files[:5]:
            file_path = os.path.join(data_folder, file)
            df = pd.read_csv(file_path)
            dataframes.append(df)
            
        return dataframes
    
    except Exception as e:
        print(f"Error loading CSV files: {str(e)}")
        return None


def display_data(dataframes):
    """
    Displays the data from each DataFrame in the list
    Args:
        dataframes: List of pandas DataFrames to display
    """
    try:
        if dataframes is None or len(dataframes) == 0:
            print("No data to display")
            return
            
        for i, df in enumerate(dataframes):
            print(f"\nDataset {i+1}:")
            print("Shape:", df.shape)
            print("\nFirst 5 rows:")
            print(df.head())
            print("\nDataset Info:")
            print(df.info())
            print("\n" + "="*50)
            
    except Exception as e:
        print(f"Error displaying data: {str(e)}")


# Load the CSV files
dataframes = load_csv_files()

# Display the data
display_data(dataframes)
