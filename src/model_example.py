from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Example model for fraud detection
def train_model(X, y):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_val, y_val, test_size=0.5, random_state=42)
    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, preds)}")
    print(f"Precision: {precision_score(y_test, preds)}")
    print(f"Recall: {recall_score(y_test, preds)}")
    return model

if __name__ == "__main__":
    # Sample data for fraud detection
    import pandas as pd
    data = {'amount': [100, 200, 50, 300, 150], 'time': [1, 2, 3, 4, 5], 'target': [0, 1, 0, 1, 0]}
    df = pd.DataFrame(data)
    X = df[['amount', 'time']]
    y = df['target']
    model = train_model(X, y)
