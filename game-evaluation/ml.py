import numpy as np
import tensorflow.keras as keras
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

print("loading data")
X = np.load("F:\\Dataset\\chess\\X.npy")
Y = np.load("F:\\Dataset\\chess\\Y.npy")
Y = (np.argmax(Y, axis=1) == 1) * 1.0

print(len(X), len(X[0]))

# kernel_regularizer=keras.regularizers.L1(0.001),
model = keras.Sequential()
model.add(keras.layers.Dense(516, activation="tanh", input_shape=(len(X[0]),)))
model.add(keras.layers.Dense(256, activation="tanh"))
model.add(keras.layers.Dense(1, activation="sigmoid"))

opt = keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='binary_crossentropy', optimizer=opt, metrics=["accuracy"])

model.summary()


split = int(len(X)*0.75)
X_, Y_ = shuffle(X[0:split], Y[0:split], random_state=0)

hist = model.fit(X_, Y_, batch_size=516, epochs=10, validation_data=(X[split:len(X)], Y[split:len(Y)]),)

plt.title("Loss over time")
plt.plot(hist.history["loss"], label="Train loss")
plt.plot(hist.history["val_loss"], label="Validation loss")
plt.legend()
plt.show()

plt.title("Accuracy over time")
plt.plot(hist.history["accuracy"], label="Train accuracy")
plt.plot(hist.history["val_accuracy"], label="Validation accuracy")
plt.legend()
plt.show()