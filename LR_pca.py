#！/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import numpy as np
#CLASSIC MULTIVARIATE LINEAR REGRESSION FORM: y = f(X) = W*X + b
#CAPITAL LETTER denotes vector, lowercase letter denotes scalar
Xy = np.genfromtxt("sheet.csv", delimiter=",")
m = len(Xy)     #rows
X = Xy[...,:-1] #size of m × n-1 
y = Xy[...,-1]  #size of m × 1
X1 = np.append(X, np.ones((m,1)), axis=1)
#ALGORITHM
X1_tp = X1.transpose()
wb = np.linalg.inv(X1_tp @ X1) @ X1_tp @ y
#OUTPUT
for i in range(len(wb)):
	if i != len(wb)-1:
		print("w_%i = %.4f" % (i, wb[i]))
	else:
		print("b = %.4f" % wb[i])