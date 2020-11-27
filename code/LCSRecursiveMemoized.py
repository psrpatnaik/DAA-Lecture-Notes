# str1=”xyu”, str2=”xy”
# We have this:LCS (str1, str2) → 2
# Case 1: str1+”z”, str2+”z” , str1=”xyuz”, str2=”xyz”
# LCS (str1+”z”, str2+”z”) = LCS (str1, str2) + 1
# Case 2: str1+”v”, str2+”u”, str1=”xyuv”, str2=”xyzu”
# LCS (str1+”u”, str2+”v”): max (LCS(“xyu”+”v”, “xy”) OR LCS(“xyu”, “xyu”))
# n,m --> 4
memoization = { } # to store the computed values for LCS method call
sequence={}
def LCS(str1, str2, n,m):
    # base case
    if(n ==0 or m==0):
        return 0
    else:
        # check if this call with n and m was already made
        if( memoization.get((n,m),-1) != -1):
            return memoization.get((n,m))
        # check if last character of both strings match
        if( str1[n-1] == str2[m-1]):
            sequence[n-1] = str1[n-1] # store the matched character in a dictionary
            # with the key as index of matched character
            memoization[(n, m)] = 1 + LCS(str1,str2, n-1, m-1)
            return memoization[(n, m)]
        else:
            #reduce the problem and get max LCS from the subproblems
            value1 = LCS(str1, str2, n - 1, m)
            value2 = LCS(str1, str2, n, m - 1)
            memoization[(n, m)] = max (value1, value2 )
            return memoization[(n, m)]

# str1 = "afgrjkl"
# str2 = "afrzxjmnk"
str1 = "abcdasdf"
str2 = "asdwe"
# a f r j k
# str1 = "aaa"
# str2 = "bbb"
# @Akash
# Sir,can you Try the  test case ?
# Str1="abcdasdf"
# Str2="asdwe"
# And check sequence
# 3
# Sequence: {0: 'a', 3: 'd', 4: 'a', 5: 's', 6: 'd'}


print(LCS(str1,str2, len(str1), len(str2)))
# print(memoization)
print("Sequence: "+ str(sequence))

# H/W:
# 1 : print the values in the dictionary in order of keys
# 2 : store the values in a dictionary like container in Python which will preserve the order
#     in which the values are inserted. That container is inside collection. OrderedDict




