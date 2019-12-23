# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
#import pickle
# load the dataset
dataset = loadtxt('Heart.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:13]
y = dataset[:,13]

# define the keras model
model = Sequential()
model.add(Dense(60, input_dim=13, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(35, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
 	
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset without progress bars
# fit the keras model on the dataset
model.fit(X, y, epochs=1000, batch_size=32)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

# make class predictions with the model
predictions = model.predict_classes(X)
# summarize the first 5 cases
for i in range(5):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))
    
#pickle.dump(model, open('..\Models\heartModel.pkl','wb'))

model.save('..\Models\heartdiseaseModel.h5')