#！/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
#求向量之范数的函数
def norm(A):
	sum = 0
	for i in A:
		sum += i**2
		normA = math.sqrt(sum)
	return normA

#创建零矩阵，单个参数为列向量，二元数组时为矩阵
def nullMat(row, col=1):
	if col == 1:
		A = [0]*row
	else:
		A = [[0]*col]*row
	return A

#默认将矩阵A当成是已转置的（不要真的去转置它！）
def matProduct(A, B):
	if len(A) != len(B):
		print("矩阵内尺寸不合！")
	else:
		C = nullMat(len(A[0]), len(B[0]))
	return C

A = [1, 1, 1, 1]
print(isinstance(A[0], float) or isinstance(A[0], int))