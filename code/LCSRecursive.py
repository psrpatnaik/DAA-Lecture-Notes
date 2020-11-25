# str1=”xyu”, str2=”xy”
# We have this:LCS (str1, str2) → 2
# Case 1: str1+”z”, str2+”z” , str1=”xyuz”, str2=”xyz”
# LCS (str1+”z”, str2+”z”) = LCS (str1, str2) + 1
# Case 2: str1+”v”, str2+”u”, str1=”xyuv”, str2=”xyzu”
# LCS (str1+”u”, str2+”v”): max (LCS(“xyu”+”v”, “xy”) OR LCS(“xyu”, “xyu”))

def LCS(str1, str2, n,m):
    # base case
    if(n ==0 or m==0):
        return 0
    else:
        # check if last character of both strings match
        if( str1[n-1] == str2[m-1]):
            return 1 + LCS(str1,str2, n-1, m-1)
        else:
            #reduce the problem and get max LCS from the subproblems
            return max (LCS(str1, str2, n-1,m), LCS(str1, str2, n, m-1))

str1 = "afgrjkl"
str2 = "afrzxjmnk"
print(LCS(str1,str2, len(str1), len(str2)))

