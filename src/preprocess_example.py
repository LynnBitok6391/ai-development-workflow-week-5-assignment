import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Example preprocessing for fraud detection
def preprocess_data(df):
    # Handle missing values using mean imputation
    df.fillna(df.mean(numeric_only=True), inplace=True)
    # Encode categorical variables
    le = LabelEncoder()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = le.fit_transform(df[col])
    # Scale numerical features
    scaler = StandardScaler()
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df

if __name__ == "__main__":
    # Sample data for fraud detection
    data = {'amount': [100, 200, 50], 'time': [1, 2, 3], 'category': ['online', 'pos', 'online']}
    df = pd.DataFrame(data)
    processed_df = preprocess_data(df)
    print(processed_df)
