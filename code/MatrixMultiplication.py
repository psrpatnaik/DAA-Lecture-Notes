import threading
import random
import time
row=300
col=300

# a=[[1,2,3],[1,2,3],[1,2,3]]
# b=[[1,2,3],[1,2,3],[1,2,3]]
# c=[[0,0,0],[0,0,0],[0,0,0]]
a =[[random.randint(1,100) for i in range(row)] for j in range(col)]
b =[[random.randint(1,100) for i in range(row)] for j in range(col)]
c =[[0 for i in range(row)] for j in range(col)]

'''
# Sequential logic
t1=time.time()
for i in range(row):
    for j in range(col):
        c[i][j] = 0
        for k in range(col):
            c[i][j] = c[i][j] + a[i][k] * b[k][j]
t2=time.time()
print (t2-t1)
'''


# Thread based logic
def computeCell(a,b,c,i,j):
    c[i][j] =  0
    for k in range(col):
        c[i][j] = c[i][j] + a[i][k] * b[k][j]

computeThreads=[]
# initializing the threads
# t1=time.time()
for i in range(row):
    for j in range(col):
        computeThreads.append(threading.Thread(target=computeCell, args=(a,b,c,i,j)))


t1=time.time()
# invoke threads
for thread in computeThreads:
    thread.start()

for thread in computeThreads:
    if(thread.isAlive()):
        thread.join()

t2=time.time()
print(t2-t1)
# output the resultant matrix
# print(c)


