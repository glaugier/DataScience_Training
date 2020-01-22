## Logistic regression derivative computation

# Requirements
import numpy as np

#Initialisation
m: int=10 # Training set size
n=12288 # Size of a single input object (64x64px colour picture)

# Parameters
a=sigmoid(z)
b=0
Wt=np.zeros(n, 1).transpose((1, 0))+b
def Loss(a, y):
    return -(y*log(a)+(1-y)*log(1-a))


J=0 # Cost function
db=0 # Derivative of the offset parameter
dw=np.zeros((n, 1))

for i in 1 to m:
    Z[i] = W.transpose((1,0))*X[i]+b
    A[i] = sigmoid(Z[i])
    J += -(Y[i]*log(Yhat[i])+(1-Y[i])*log(1-Y[i]))
    da_dz[i]=A[i]*(1-A[i])
    dw+=X[i]*da_dz[i]

# Computing the averages
J /= m
dw /= m
db /= m