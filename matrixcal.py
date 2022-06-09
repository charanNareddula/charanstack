import numpy as np
import random
import time
class Matrix:
    def __init__(self, rows, columns):
        self.rows = 10
        self.columns= 10
        type = 2
        #self.mat = [[123.5 for c in range(self.columns)] for row in range(self.rows)]
        if type ==1:
            self.mat = np.array([[123.5 for c in range(self.columns)] for row in range(self.rows)],dtype='f')
        else:
            self.mat = [[123.5 for c in range(self.columns)] for row in range(self.rows)]
        #print(type(self.mat))
    def add(self, X,Y):
        for i in range(X.rows):
            for j in range(Y.columns):
                self.mat[i][j] = X.mat[i][j] + Y.mat[i][j]
    
    def sub(self,X,Y):
        for i in range(X.rows):
            for j in range(Y.columns):
                self.mat[i][j] = X.mat[i][j] - Y.mat[i][j]
    
    def mul(self,X,Y):
        for i in range(X.rows):
            for j in range(Y.columns):
                self.mat[i][j]=0
                for k in range(X.columns):
                    self.mat[i][j] = self.mat[i][j] + X.mat[i][k]*Y.mat[k][j]
    def mul1(self,X,Y):
        self.mat = np.matmul(X.mat,Y.mat) 
                 
    
a = Matrix(3,3)
a.mat[1][1]=5
#print(a.mat)
b = Matrix(3,3)
print(b.mat)
b.mat[1][0]=9.0
print(b.mat)
c = Matrix(3,3)
c.add(a,b)
#print(c.mat)
c.sub(a,b)
#print(c.mat)
start = time.time()
for i in range(100000):
    c.mul1(a,b)
end = time.time()
print("Time taken: ",(end-start))
print(c.mat)





