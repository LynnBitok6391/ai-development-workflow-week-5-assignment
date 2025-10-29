from sklearn.metrics import classification_report, confusion_matrix

# Example evaluation for fraud detection
def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, preds))
    print("Classification Report:")
    print(classification_report(y_test, preds))

if __name__ == "__main__":
    # Assuming model and data from model_example
    from model_example import train_model
    import pandas as pd
    data = {'amount': [100, 200, 50, 300, 150], 'time': [1, 2, 3, 4, 5], 'target': [0, 1, 0, 1, 0]}
    df = pd.DataFrame(data)
    X = df[['amount', 'time']]
    y = df['target']
    model = train_model(X, y)
    # For demo, use same data
    evaluate_model(model, X, y)
