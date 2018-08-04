#！/usr/bin/env python3
# -*- coding: utf-8 -*-
import fn
import re
#SUPPORT VECTOR MACHINE
hasFile = False
while hasFile == False:
    fileName = input("要导入的训练集文本：")
    try:
        setD = open(fileName, "r")
    except IOError:
        print("没有找到该文件，请重试")
    else:
        hasFile = True
Xy = []
for entry in setD:
    Xy.append(entry.strip())
for i in range(len(Xy)):
    Xy[i] = re.split(r'\s+', Xy[i].strip())
setD.close()
m = len(Xy) #rows of [X|y], i.e. number of entries
n = len(Xy[0]) #columns of [X|y]
X = []
y = []
for i in range(m):
    X.append([])
    for j in range(n-1):
        X[i].append(float(Xy[i][j]))
    y.append(float(Xy[i][-1]))
#MAIN ALGORITHM
wx = fn.nullMatrix(m)
for i in range(m):
    for j in range(n-1):
        wx[i] = pass
r = pass
print(X, y)
