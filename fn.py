#！/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from io import StringIO
AB = np.genfromtxt("sheet.csv", delimiter=",", dtype=float)
a = AB[...,:-1]
print(a)
n = np.ones((3,1))
print(n)
b = np.append(a, n, axis=1)
print(b)