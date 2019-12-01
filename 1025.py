import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def meanX(dataX):
    return np.mean(dataX,axis=0)
def pca(XMat, k):
    average = meanX(XMat)
    m, n = np.shape(XMat)
    print(m,n,average)
    aj=[]
    av=np.tile(average,(m,1))
    print(XMat,'\n*************\n',av)
    aj=XMat-av
    print(aj,'\n*************---\n',aj.T)
    covx=np.cov(aj.T)
    print(covx)
    featValue, featVec = np.linalg.eig(covx)
    print(featValue,'\n*************+++\n',featVec)
    index = np.argsort(-featValue)
    print(index[:k])
    fd=[]
    selectVec = np.matrix(featVec.T[index[:k]])
    finalData = aj * selectVec.T
    print(selectVec.T,'\n***+++*******+++\n',finalData)
    reconData = (finalData * selectVec)+average
    print(reconData)

sj62=np.array([[9,8,5],[5,8,4],[6,7,3],[2,4,7]])
sj63=np.array([[2.5,2.4],[0.5,0.7],[2.2,2.9],[1.9,2.2],[3.1,3],[2.3,2.7],[2,1.6],[1,1.1],[1.5,1.6],[1.1,0.9]])
dir(copy.copy)
print(sj62,'\n****************')
#pca(sj63,1)
