import numpy as np
import pandas as pd

def load_data(file_path, **kwargs):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path, **kwargs)
    elif file_path.endswith('.npy'):
        return np.load(file_path, **kwargs)
    else:
        raise ValueError('Invalid file format')

def preprocess_data(data, **kwargs):
    if 'normalize' in kwargs and kwargs['normalize']:
        return (data - data.mean()) / data.std()
    else:
        return data

def evaluate_anomaly_detector(detector, X, y):
    y_pred = detector.predict(X)
    accuracy = np.mean(y == y_pred)
    precision = np.mean(y[y_pred == 1] == 1)
    recall = np.mean(y_pred[y == 1] == 1)
    f1 = 2 * (precision * recall) / (precision + recall)
    return accuracy, precision, recall, f1
