import time
import os
from visualiser.visualiser import Visualiser as vs
os.environ["PATH"] += os.pathsep + 'D:\\Softwares\\Graphviz\\bin'

# 0 1 1 2 3 5 8 13 ......
n=6
memoization_array = [-1]*(n+1)
# memoization_array [0]=0
# memoization_array [1]=1
@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def fib(n=n):
    if n <= 1:
        return n
    else:
        # Memoization , we store the previously computed values
        # and use them instead of computing again
        if memoization_array[n] == -1:
            return_value = fib(n=n-1) + fib(n=n-2)
            memoization_array[n] = return_value
            return return_value
        else:
            return memoization_array[n]
#print (fib(6))

t1=time.time()
x=fib(n=n)
t2=time.time()
print(str(t2-t1))
vs.make_animation()
