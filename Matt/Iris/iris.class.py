from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from keras.models import Sequential
from keras.layers import Dense, Dropout
from tensorflow import keras

import numpy as np
import seaborn as sns
import pandas as pd

class IrisClassifier:
    def __init__(self, data_path='./data/Iris.csv'):
        self.data_path = data_path
        self.data_frame = None
        self.le = LabelEncoder()
        self.x = None
        self.y = None
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None
        self.model = None
    
    def load_data(self):
        self.data_frame = pd.read_csv(self.data_path)

    def preprocess_data(self):
        self.le.fit(self.data_frame['Species'])
        self.data_frame['Species'] = self.le.transform(self.data_frame['Species'])