import numpy as np
import tensorflow.keras as keras
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

print("loading data")
X = np.load("./X.npy")
Y = np.load("./Y.npy")

print(len(X), len(X[0]))

# kernel_regularizer=keras.regularizers.L1(0.001),
model = keras.Sequential()
#model.add(keras.layers.Dense(128, activation="relu", input_shape=(len(X[0]),)))
#model.add(keras.layers.Dense(92, activation="relu"))
#model.add(keras.layers.Dense(64, activation="relu"))
#model.add(keras.layers.Dense(3, activation="sigmoid"))
model.add(keras.layers.Dense(3, activation="sigmoid", input_shape=(len(X[0]),)))

opt = keras.optimizers.Adam(learning_rate=0.0001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=["accuracy"])

model.summary()


split = int(len(X)*0.75)


X_, Y_ = shuffle(X[0:split], Y[0:split], random_state=0)

hist = model.fit(X_, Y_, batch_size=128, epochs=50, validation_data=(X[split:len(X)], Y[split:len(Y)]),)

plt.plot(hist.history["loss"])
plt.plot(hist.history["val_loss"])
plt.show()

plt.plot(hist.history["accuracy"])
plt.plot(hist.history["val_accuracy"])
plt.show()