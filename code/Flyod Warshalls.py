# 999 is used to represent infinity, arbitrarily large value
A = [[0,4,5], [2,0,999], [999,3,0]]
# n is number of nodes in graph
n = 3
print(A)
# Floyd's Algorithm
#main->row->column
for i in range(n):
    for r in range(n):
        for c in range(n):
            A[r][c] = min (A[r][c], (A[r][i] + A[i][c]))
print("Final matrix")
print(A)



