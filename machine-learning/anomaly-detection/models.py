import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.neighbors import LocalOutlierFactor
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class AnomalyDetector:
    def __init__(self, model_type, **kwargs):
        self.model_type = model_type
        self.kwargs = kwargs
        self.model = self._get_model()

    def _get_model(self):
        if self.model_type == 'isolation_forest':
            return IsolationForest(**self.kwargs)
        elif self.model_type == 'one_class_svm':
            return OneClassSVM(**self.kwargs)
        elif self.model_type == 'local_outlier_factor':
            return LocalOutlierFactor(**self.kwargs)
        elif self.model_type == 'lstm_autoencoder':
            return self._get_lstm_autoencoder_model()
        else:
            raise ValueError('Invalid model type')

    def _get_lstm_autoencoder_model(self):
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True, input_shape=(self.kwargs['input_shape'][0], self.kwargs['input_shape'][1])))
        model.add(LSTM(units=50))
        model.add(Dense(self.kwargs['input_shape'][1]))
        model.compile(loss='mean_squared_error', optimizer='adam')
        return model

    def fit(self, X):
        self.model.fit(X)

    def predict(self, X):
        if self.model_type == 'lstm_autoencoder':
            return self.model.predict(X)
        else:
            return self.model.predict(X).reshape(-1)

    def score(self, X):
        if self.model_type == 'lstm_autoencoder':
            return self.model.evaluate(X, X)
        else:
            return self.model.decision_function(X)

class LSTMAnomalyDetector(AnomalyDetector):
    def __init__(self, **kwargs):
        super().__init__('lstm_autoencoder', **kwargs)

class IsolationForestAnomalyDetector(AnomalyDetector):
    def __init__(self, **kwargs):
        super().__init__('isolation_forest', **kwargs)

class OneClassSVMAnomalyDetector(AnomalyDetector):
    def __init__(self, **kwargs):
        super().__init__('one_class_svm', **kwargs)

class LocalOutlierFactorAnomalyDetector(AnomalyDetector):
    def __init__(self, **kwargs):
        super().__init__('local_outlier_factor', **kwargs)
