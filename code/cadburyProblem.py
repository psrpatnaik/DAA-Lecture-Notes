# M, N, P, Q
memoization={}
'''
# Recursive logic
def getCountRecursive(l, b):
    x = 0
    y = 0
    x = min(l, b)
    y = max(l, b)
    # check if getCountRecursive for x and y was previously computed?
    if memoization.get((x,y),-1) != -1:
        #print("A")
        return memoization.get(x,y)
    else:
        #print("B")
        # Base cases of the recursion
        # If either length or breadth is 1 no need for computing
        if(x == 1):
            return y
        if(y == 1):
            return x
        # when length and breadth are same it is a square
        if (x == y):
            return 1
        else:
            # if(l<b):
            #     count = 1 +  getCountRecursive(l, b-l)
            #     return count
            # else:
            #     count = 1 + getCountRecursive(l-b, b)
            #     return count
            count = 1 + getCountRecursive(x, y - x)
            # X = 3 , Y = 7, How many times the method gets called ? and with what values 
            # X and Y ?
            # Store the result in memoization data structure
            memoization[(x,y)] = count
            return count
'''
# Iterative
def getCountIterative(l, b):
    x = 0
    y = 0
    x = min(l, b)
    y = max(l, b)
    if (x == 1):
        return y
    if (y == 1):
        return x
        # when length and breadth are same it is a square
    if (x == y):
        return 1
    else:
        count = 0
        '''
        # A
        while ( x != y):
            print("X:"+str(x)+" Y:"+str(y))
            # Code goes here
            # y = 7 , x = 3 ----> 1 7X3 4X3 , 1X3, ......
            # y = 8 , x = 3 ----> 2 8x3 , 5x3, 2x3, 1X2
            # y = 8 , x = 4 ----> 0 8x4 , 4x4.
            # x = y-x
            y = y - x
            # Swap the values
            if (y < x):
                t = x
                x = y
                y = t
            count = count + 1
        '''
        # division , q and r
        # B
        while (x !=0):
            q = y // x
            r = y % x
            count = count + q
            y = x
            x = r
            # check if you have already computed value for the new x and y ?
        return count
'''
Shared by Akash
While(y//x !=1)
  Count+=(y//x)
  Temp=x
  x=y-(y % x)
  y=Temp
'''
# M, N, P, Q= 3 ,4 , 4, 5
# M, N, P, Q= 5 ,7 , 3, 4
# 7 X 3 (5) , 7 X 4 (5)
# totalCount=0
# for i in range(M, N+1):
#     for j in range (P, Q+1):
#         totalCount = totalCount + getCountRecursive(i, j)
# print(totalCount)
# print(memoization)
# print(getCountRecursive(3,4))
# print(getCountRecursive(4,3))
print(getCountIterative(3,7)) # 5
print(getCountIterative(3,8)) # 5
print(getCountIterative(4,8)) # 2
print(getCountIterative(4,9)) # 3 ---- > (4,5)
# print(memoization)

# without memoization: O(2^N) almost a exponential
# without memoization: O((N-M) * (Q-P)) a polynomial order


