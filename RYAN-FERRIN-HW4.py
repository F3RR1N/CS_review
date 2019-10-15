# HW4 assignment
# Ryan Ferrin
# WPI CS5007 F19
# October 16, 2019

import matplotlib.pyplot as plt
import numpy as np
import math

# 1) Archimedean spiral

def arc():
    t = np.arange(0, 5*np.pi, .01)
    x = t*np.cos(t)
    y = t*np.sin(t)

    plt.plot(x, y, 'g')
    plt.show()

plt.figure(1)
arc()

#  2) Heart

def heart():

    t = np.arange(0, 2*np.pi, .01)
    x = 16*(np.sin(t)**3)
    y = 13*np.cos(t) - 5*np.cos(2*t) - 2.5*np.cos(3*t) - np.cos(4*t)

    plt.plot(x, y, 'r--')
    plt.show()

plt.figure(2)
heart()

# 3) graphs

# to solve the chemicals transportation problem using graph theory,
# the vertices1, P4-Pk. would be the chemicals, P1, P2, . . Pk. the edges would be the safe travel partners.
# some examples would be: for P1 the edges would be P1-P3, P1-P4, P1-P5, ... P1-Pk-1

# The Graph property is

class Graph:
    def __init__(self,k):
        self.k = k
        self.edges = self.buildMatrix()

    def buildMatrix(self):

        res = []
        for i in range(0,self.k):
            col = []
            for j in range(0,self.k):
                col.append(0)
            res.append(col)
        return res

    def toString(self):
        s = ''
        for e in self.edges:
            s += str(e)+'\n'
        return s

    def addEdge(self, i, j):
        try:
            self.edges[i][j]=1
        except IndexError:
            print('Could not add edge ('+str(i)+','+str(j)+')')
            print('Index error')

    def removeEdge(self, i, j):
        try:
            self.edges[i][j]=0
        except IndexError:
            print('Could not remove edge ('+str(i)+','+str(j)+')')
            print('Index error')


class UnGraphWtLoop(Graph):
    def __init__(self,n):
        Graph.__init__(self,n)

    def addEdge(self,i,j):
        if(i==j):
            print('addEdge(self,i,j): No loop')
            return
        try:
            self.edges[i][j]=1
            self.edges[j][i]=1
        except IndexError:
            print('Could not add edge ('+str(i)+','+str(j)+')')
            print('Index error')

    def removeEdge(self, i, j):
        try:
            self.edges[i][j] = 0
            self.edges[j][i] = 0
        except IndexError:
            print('Could not remove edge (' + str(i) + ',' + str(j) + ')')
            print('Index error')

class Shippment:
    def __init__(self, graph):



g = UnGraphWtLoop(7)
print(g.toString())

for i in range(0, g.k):
    for j in range(0, g.k):
        if i == j or j == i+1 or j == i-1:
            g.removeEdge(i, j)
        elif (i == 0 and j == g.k - 1) or (i == g.k - 1 and j == 0):
            g.removeEdge(i, j)
        else:
            g.addEdge(i, j)

print(g.toString())


# 4) Egyptian Multiplicaton

def egyptmult(x, y):
    if x < 0 or y < 0:
        print('positive values only')
    elif x <= 2 or y <= 2:
        return x * y
    elif y%2 == 0:
        return 2 * egyptmult(x, y//2)
    else:
        return x + egyptmult(x, y-1)

print(egyptmult(7, 10))