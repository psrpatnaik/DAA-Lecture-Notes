# [ [p,w], [p,w] .....]
items=[[1,1],[6,2],[10,3],[16,5]]
#items=[[40,20],[100,10],[50,40],[60,30]] # n
# M denotes max knapsack capacity C
M=7
#M=60 # C
# Tabulation approach
# Tabulation method START
# Create the table and initialization of Table
# table= [[0]*(M+1)]*(len(items)+1)  # A
table=[[0]*(M+1) for i in range(len(items)+1)] # B
# deep copy and shallow copy.
def maxprofitTabulation(items, capacity):
    for i in range(1,len(items)+1):
        for j in range(1,M+1):
            profitItemIncluded = 0
            profitItemExcluded = 0
            if(items[i-1][1] <= j):
                profitItemIncluded = items[i-1][0] + table[i-1][j- items[i-1][1]]
            profitItemExcluded = table[i-1][j]
            table[i][j]=max(profitItemIncluded, profitItemExcluded)

maxprofitTabulation(items,M)
for row in table:
    print(row)

# END Tabulation method START


# 2D array of n rows and C
# (M, max capacity of Knapsack) columns
#
# memoization_table = [[-1]*(M+1)]*(len(items)+1) # A
# memoization_table = [[0]*(M+1) for i in range(len(items)+1)] # B
# print("Before")
# print(memoization_table)
#
# def maxprofit(items, capacity, index):
#     profitItemIncluded=0
#     profitItemExcluded=0
#     if capacity <= 0 or index >= len(items):
#         return 0
#     # Check if we can include the current item can be included or not
#     # Memoize the recursion calls.
#     if not memoization_table[index][capacity] == -1:
#         print("capacity:"+ str(capacity)+ "index:"+ str(index))
#         return memoization_table[index][capacity]
#     else:
#         if capacity >= items[index][1]:
#             # Calculate profit if item is included
#             profitItemIncluded = items[index][0] + maxprofit(items, capacity-items[index][1], index + 1)
#         # Calculate profit if item is excluded
#         profitItemExcluded = maxprofit(items, capacity, index + 1)
#         # Check which proft is maximum, the one after including or the one after excluding
#         # and return the max profit
#         return_value = max(profitItemIncluded, profitItemExcluded)
#         memoization_table[index][capacity] = return_value
#         return return_value
# # Call to recursive method
# print("After")
# print(str(maxprofit(items,M,0)))
# print(memoization_table)

# n*C , where is max Capacity of Knapsack
# we need 2D array of n rows and C columns
# Without memoization: O(2^n)
# With memoization: O(n*C) where C is max capacity and n is input size.





