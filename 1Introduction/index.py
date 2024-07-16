import cv2 as cv
print(cv.__version__)
img01=cv.imread('./flowers.jpeg')
from matplotlib import pyplot as plt
plt.imshow(cv.cvtColor(img01,cv.COLOR_BGR2RGB))
img02=cv.imread('./flowers.jpeg',cv.IMREAD_GRAYSCALE)
plt.imshow(cv.cvtColor(img02,cv.COLOR_BGR2RGB))
plt.imshow(cv.cvtColor(img02,cv.COLOR_BGR2RGB))
img01.shape[2]
img02.shape
h,w,_= img01.shape
for i in range(300,450):
    for j in range(400,700):
        img01[i,j]=(0,0,200)
plt.imshow(cv.cvtColor(img01,cv.COLOR_BGR2RGB))
hist=[0 for i in range(256)]
for i in range(100,200):
    for j in range(100,200):
        color=img02[i,j]
        hist[color]+=1
        
plt.plot(hist)
 
plt.rcParams['figure.figsize']=[10,5]
plt.bar(range(256),hist)
import os
os.getcwd()

histR=[0 for i in range(256)]
histG=[0 for i in range(256)]
histB=[0 for i in range(256)]
B,G,R= cv.split(img01)
for i in range(100,200):
    for j in range(100,200):
        blue=(B[i,j])
        red=(R[i,j])
        green=(G[i,j])
        histR[red]+=1
        histG[green]+=1
        histB[blue]+=1
plt.plot(histB)
plt.plot(histR)
plt.plot(histG)