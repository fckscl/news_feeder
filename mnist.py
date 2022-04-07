from tensorflow.keras.datasets import mnist
from tensorflow import keras
import tensorflow.keras.models
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# стандартизация входных данных
x_train = x_train / 255
x_test = x_test / 255
y_train_cat = keras.utils.to_categorical(y_train, 10)
y_test_cat = keras.utils.to_categorical(y_test, 10)

model = tensorflow.keras.models.load_model('E:\AI\python\\neyro\model_num')
n = 2
x = np.expand_dims(x_test[n], axis=0)
res = model.predict(x)
res = np.argmax(res)
#print( res )
#print( np.argmax(res) )
