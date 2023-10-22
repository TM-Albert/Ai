import numpy as np
import seaborn as sns
import pandas as pd
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

data_frame = pd.read_csv('./data/Iris.csv')

# print the quantity of each column values

print(data_frame['SepalLengthCm'].value_counts())
print(data_frame['SepalWidthCm'].value_counts())
print(data_frame['PetalLengthCm'].value_counts())
print(data_frame['PetalWidthCm'].value_counts())
print(data_frame['Species'].value_counts())

print(data_frame.isnull().sum())

print(data_frame.head(5))

# convert the species column to numeric values
le = LabelEncoder()
data_frame['Species'] = le.fit_transform(data_frame['Species'])

species_name = le.classes_

print(le.classes_)

print(data_frame.head(5))

x = data_frame.drop(columns=['Id', 'Species'])
y = data_frame['Species']

print(x.head(5))
print(y.head(5))