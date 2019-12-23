# -*- coding: utf-8 -*-
"""
Creating the model
"""

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
#import pickle


# load the dataset
dataset = loadtxt(r'diabetes.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]


# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(X, y, epochs=10000, batch_size=64)

# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

predictions = model.predict_classes(X)
# summarize the first 5 cases
for i in range(5):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))


#pickle.dump(model, open('..\Models\diabetesModel.pkl','wb'))
model.save('..\Models\diabetesModel.h5')