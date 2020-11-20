# Nodes: 10,  12,  16, 21
# Freq     4,     2,    6,  3
# keys = [10,12,16,21]
# freq = [4,2,6,3]

keys=[1,2,3,4]
freq=[1,2,4,3]
# 17

# to store the computed values (i,j): cost of BST from node i to j
cost = {}

# initialization
for i in range (len(keys)):
    cost[(i,i)]= freq[i]

# our containers are 0 indexed
size = 1

# cost(i,j) = sum (freq of i to j) +
# min (
# cost (i+1,j) → 1st node i as root,
# cost(i,i) + cost (i+2,j) → 2nd node i+1 as root,
# cost(i,i+1) + cost (i+3,j) → 3rd node i+2 as root,
# .
# .
# cost (i,j-1) → last node j as root
# )

while ( cost.get((0,len(keys)-1),-1) == -1):
    for i in range(len(keys)-size):
        min_list =[]
        min_list.append(cost[(i+1,i+size)]) # 1st node being root
        min_list.append(cost[(i , i + size-1)]) # last node being root
        # add all intermediete nodes as root elements
        for k in range(i+1, i+size):
            min_list.append(cost[(i , k-1)] + cost[(k+1 , i+size)])
        cost[(i, i+size)] = sum(freq[i: i+size+1]) + min (min_list)
    size+=1

print(cost[0,len(keys)-1])
# O(n^3) by using bottom up approach of Dynamic Programming

