import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.callbacks import TensorBoard
import matplotlib.pyplot as plt
from keras import optimizers
import random

with open('dataset.csv') as f:
    data = f.readlines()
X = []
y = []
# print(len(data))
# random.shuffle(data)
for row in data:
    row = row.split(',')
    ipbit = list(map(int,list(row[0])))
#     ipbit = list(map(int,row[0].split('.')))
    tp = row[1].strip()
    tp = float(tp)
    tp = int(tp)
    X.append(ipbit)
    y.append(tp)

X = np.array(X)
y = np.array(y)


tensorboard = TensorBoard(log_dir='.\logs')

X_train,y_train = X[:8000],y[:8000]
X_test,y_test = X[8000:],y[8000:]

learning_rate = 0.01
adam = optimizers.Adam(lr=learning_rate)

model = Sequential()
model.add(Dense(output_dim = 64,input_dim=32,activation='relu'))
model.add(Dense(output_dim = 128,activation='relu'))
model.add(Dense(output_dim = 256,activation='relu'))
model.add(Dense(output_dim = 256, activation='relu'))
model.add(Dense(output_dim = 128, activation='relu'))
model.add(Dense(output_dim = 64, activation='relu'))
model.add(Dense(output_dim = 32, activation='relu'))
model.add(Dense(output_dim = 1, activation='relu'))
model.compile(optimizer='adam', loss='mae')

trainloss = []
testloss = []
epochs = 100
print('--------Training-------')
for i in range(epochs):
    his = model.fit(X_train,y_train,batch_size=64,shuffle=False,
        validation_split=0.05)
    res = model.evaluate(X_test,y_test,batch_size=32)
    trainloss.append(his.history['loss'][0])
    testloss.append(res)
    # axis = range(i+1)
    # ln1,=plt.plot(axis,testloss,c='r')
    # ln2,=plt.plot(axis,trainloss,c='g')
    # plt.show()
    # if i!=20:
    #     ln1.remove()
    #     ln2.remove()

print('train finish')

# print(his.history['loss'])
ANS = model.predict(X_test[-10:])
print(ANS)
axis = range(epochs)
plt.plot(axis,testloss,c='r')
plt.plot(axis,trainloss,c='g')
plt.show()
print('---------TEST----------')
res = model.evaluate(X_test,y_test,batch_size=64)
print(res)
