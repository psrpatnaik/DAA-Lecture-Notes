# [ [p,w], [p,w] .....]
# items=[[1,1],[6,2],[10,3],[16,5]]
items=[[40,20],[100,10],[50,40],[60,30]]
# M denotes max knapsack capacity C
# M=7
M=60

def maxprofit(items, capacity, index):
    profitItemIncluded=0
    profitItemExcluded=0
    if capacity <= 0 or index >= len(items):
        return 0
    # Check if we can include the current item can be included or not
    if capacity >= items[index][1]:
        # Calculate profit if item is included
        profitItemIncluded = items[index][0] + maxprofit(items, capacity-items[index][1], index + 1)
    # Calculate profit if item is excluded
    profitItemExcluded = maxprofit(items, capacity, index + 1)
    # Check which proft is maximum, the one after including or the one after excluding
    # and return the max profit
    return max(profitItemIncluded, profitItemExcluded)

# Call to recursive method
print(str(maxprofit(items,M,0)))
