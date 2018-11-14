#convergence

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#read
def readData(filename):
	df=pd.read_csv(filename)
	return df.values
x=readData('I:\ml-workshop-pec-chandigarh-master\data\linearX.csv')
#x=x.reshape((99,))
x=x-(x.mean())/x.std()
y=readData('I:\ml-workshop-pec-chandigarh-master\data\linearY.csv')
#y=y.reshape((99,))
print(x.shape)
print(y.shape)
plt.scatter(x,y)
plt.show()

def hypothesis(theta,x):
	return theta[0]+theta[1]*x
def error(X,Y,theta):
	e=0
	for i in range(x.shape[0]):
		e+=(Y[i]-hypothesis(theta,X[i]))**2
		return 0.5*e

def gradient(Y,X,theta):
	grad=np.array([0.0,0.0])
	#sum of gradients	
	for i in range(X.shape[0]):
		grad[0]+=(Y[i]-hypothesis(theta,X[i]))
		grad[1]+=(Y[i]-hypothesis(theta,X[i]))*X[i]
	return grad

def gradientDescent (X,Y,learning_rate,maxItr):
	theta=np.array([0.0,0.0])
	grad=np.array([0.0,0.0])

	for i in range(maxItr):
		grad=gradient(Y,X,theta)
		#update theta
		theta[0]=theta[0]+learning_rate*grad[0]
		theta[1]=theta[1]+learning_rate*grad[1]
	return theta
theta=gradientDescent(x,y,learning_rate=0.2,maxItr=100)
print (theta)
plt.scatter(x,y)
plt.plot(x,hypothesis(theta,x))
plt.show()


