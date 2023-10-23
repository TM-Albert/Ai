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


iris = pd.read_csv('./data/Iris.csv')

# convert the species column to numeric values
le = LabelEncoder()
iris['Species'] = le.fit_transform(iris['Species'])

species_name = le.classes_

x = iris.drop(columns=['Id', 'Species'])
y = iris['Species']

print(x.head(5))
print(y.head(5))

# 30% of the data will be used for testing and 70% for training
# the data is randomly split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

print(x_train.shape)

sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

y_train = keras.utils.to_categorical(y_train, num_classes=3)

model = Sequential()
model.add(Dense(units=32, activation='relu', input_shape=(x_train.shape[-1], )))
model.add(Dense(units=32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=3, activation='softmax'))

model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

model.fit(x_train, y_train, epochs=1000, verbose=2)

# predict the test data

prediction = model.predict(x_test)
prediction = np.argmax(prediction, axis=-1)

cm = confusion_matrix(y_test, prediction)

print(prediction[:5])

print(accuracy_score(y_test, prediction))
print(cm)