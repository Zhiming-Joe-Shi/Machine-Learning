#！/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
#CLASSIC MULTIVARIABLE LINEAR REGRESSION FORM: y = f(X) = W*X + b
#CAPITAL LETTER denotes vector, lowercase letter denotes scalar
X, y = [], []
Xy = [] #an m × n augmented matrix [X|y]
#read training set data from a txt file
for entry in open("array.txt"):
    Xy.append(entry.strip())
for i in range(len(Xy)):
    Xy[i] = re.split(r'\s+', Xy[i].strip())
m = len(Xy) #rows of [X|y], i.e. number of entries
n = len(Xy[0]) #columns of [X|y]
#break the augmented matrix [X|y] into X and y
for i in range(m):
    X.append([])
    for j in range(n-1):
        X[i].append(float(Xy[i][j]))
    y.append(float(Xy[i][-1]))
W, b = [0]*(n-1), 0 #size of W is dependent on size of X
#set STEP_SIZE, a.k.a. learning rate
STEP_SIZE = float(input("Set your learning rate. STEP_SIZE = "))
#ALGORITHM
isMin = False
prevDistSum = None
while isMin == False:
    dW = [0]*(n-1) #(re-)initialize local variables
    db = 0
    wx = [0]*(m)
    distSum = 0
    for j in range(n-1):
        for i in range(m):
            wx[i] += W[j]*X[i][j]
            dW[j] += (1/m)*X[i][j]*(wx[i] + b - y[i])
    for i in range(m):
        db += (1/m)*(wx[i] + b - y[i])
        distSum += (1/(2*m))*(wx[i] + b - y[i])**2
    if prevDistSum == None or distSum / prevDistSum <= 0.9999999999:
        prevDistSum = distSum
        for j in range(n-1):
            W[j] -= STEP_SIZE * dW[j]
        b -= STEP_SIZE * db
    elif distSum / prevDistSum > 0.9999999999:
        isMin = True
#print out the outputs
print("---OUTPUT---")
for i, val in enumerate(W):
    print("w_%d = %.4f" % (i+1, val))
print("b = %.4f" % b)
print("The minimized squared sum = %.4f" % distSum)
#Author: Zhiming Shi