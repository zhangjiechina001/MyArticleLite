from __future__ import print_function

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers  import Dense,Dropout
from keras.optimizers import RMSprop

batch_size=128
num_class=10
epochs=20

(x_train,y_train),(x_test,y_test)=mnist.load_data(path=r'C:\Users\Administrator\PycharmProjects\MyPython\pyQt5\mnist.npz')

x_train=x_train.reshape(60000,784)
x_test=x_test.reshape(10000,784)
x_train=x_train.astype('float32')
x_test=x_test.astype('float32')
x_train=x_train/255
x_test=x_test/255
print (x_train.shape[0],'trainsamples')
print (x_test.shape,'testsamples')

y_train=keras.utils.to_categorical(y_train,num_class)
y_test=keras.utils.to_categorical(y_test,num_class)

model=Sequential()
model.add(Dense(512,activation='relu',input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(512,activation='relu',use_bias=True))
model.add(Dropout(0.2))
model.add(Dense(256,activation='relu'))
model.add((Dropout(0.1)))
model.add(Dense(num_class,activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',optimizer=RMSprop(),metrics=['accuracy'])

history=model.fit(x_train,y_train,batch_size,epochs,verbose=1,validation_data=(x_test,y_test))

score=model.evaluate(x_test,y_test,verbose=0)
print('Test loss:',score[0])
print('Test accuracy:',score[1])

