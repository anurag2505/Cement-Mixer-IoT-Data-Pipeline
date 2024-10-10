import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from data_cleaner import clean_data

def normalize_data(df):
    scaler = MinMaxScaler()
    normalized_df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return normalized_df

if __name__ == "__main__":
    # Assuming clean_data function returns a DataFrame
    df = clean_data()
    normalized_df = normalize_data(df)
    print(normalized_df.head())