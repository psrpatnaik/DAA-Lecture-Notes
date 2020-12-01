# str1 = "afgrjkl" # ---> n
# str2 = "afrzxjmnk" # ---> m
# 5

# str1 = "aaa"
# str2 = "bbb"
# 0

str1 = "abcdasdf"
str2 = "asdwe"
# 3 asd

# A case where we have multiple LCS with same length

n = len(str1)
m = len(str2)
# create the table and initialize the values to 0
table = [[0 for i in range(m+1)] for j in range(n+1)]

# print(table)

# tabulation approach
for i in range(1,n+1):
    for j in range(1,m+1):
        # check if the last character match
        if (str1[i-1]==str2[j-1]): # since the python containers are zero indexed.
            table[i][j] = 1 + table[i-1][j-1]
        else:
            table[i][j] = max (table[i][j-1], table[i-1][j])

print("Length of LCS for {} and {} is {}".format(str1,str2,table[n][m]))

# H/W print the sequence as well for this program.
