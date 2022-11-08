import numpy as np
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import tensorflow.keras as keras

print("loading data")
X = np.load("F:\\Dataset\\chess\\X.npy")
Y = np.load("F:\\Dataset\\chess\\Y.npy")

print(len(X), len(X[0]))

model = keras.Sequential()

model.add(keras.layers.Dense(3, activation="sigmoid", input_shape=(len(X[0]),)))

opt = keras.optimizers.Adam(learning_rate=0.0001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=["accuracy"])

model.summary()

split = int(len(X)*0.75)

X_, Y_ = shuffle(X[0:split], Y[0:split], random_state=0)

hist = model.fit(X_, Y_, batch_size=128, epochs=15, validation_data=(X[split:len(X)], Y[split:len(Y)]),)

plt.plot(hist.history["loss"])
plt.plot(hist.history["val_loss"])
plt.show()

plt.plot(hist.history["accuracy"])
plt.plot(hist.history["val_accuracy"])
plt.show()

model.save("./reg-log.h5")