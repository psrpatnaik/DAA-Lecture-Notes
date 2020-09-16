#numbers=[12,-12,2,10,-2,5,-10,-9,3,4]
#numbers=[-12,-12,-2,-10,-2,-5,-10,-9,-3,-4]
#numbers=[-12,-12,2,10,-2,15,-10,-9,13,14]
#numbers=[-14,-56,9,7,-7,-56,-7,12]
#numbers=[12,-12,2,10]
#numbers=[-2,-3,-5,0]
numbers=[-11,-2,-3,-19]
subarray=[]
MaxSubArray=[]
MaxSubArraySum=0
subarraysum=0
lenOfNumbers=len(numbers)
#
# for i in range(1,lenOfNumbers): # n
#     for j in range(0, lenOfNumbers): # n
#         if(j+i < lenOfNumbers -1):
#             subarray=numbers[j:j+i]
#             #print(subarray)
#             #subarraysum=max(subarraysum, sum(subarray))
#             if(subarraysum < sum(subarray)): # approx n
#                 subarraysum = sum(subarray)
#                 MaxSubArray=subarray
# print("Max sum of subarray: "+ str (subarraysum))
# print("Max Subarray: "+ str (MaxSubArray))
# n*n*n
# O(n^3) ==> O(n^2)
# code below
#
# for i in range(0,lenOfNumbers): # n
#     subarraysum = 0
#     for j in range(i, lenOfNumbers): # n
#         subarray=numbers[i:j+1]
#         subarraysum=subarraysum + numbers[j]
#         # print("Subarray",subarray)
#         # print("Sum of subarray", subarraysum)
#         if(subarraysum >= MaxSubArraySum):
#             MaxSubArray = subarray
#             MaxSubArraySum = subarraysum
#             # print("MaxSubArraySum", MaxSubArraySum)
#             # print(" ### Max Subarray: " + str(MaxSubArray))
#
# print("Max sum of subarray: "+ str (MaxSubArraySum))
# print("Max Subarray: "+ str (MaxSubArray))
# The following is the recursive divide and conquer based approach
# with time complexity of O(n log n)

# def MaxSumSubArrayDnC(left, right, numbers):
#     if left == right:
#         return left, right, numbers[left]
#     # Divide
#     mid = (left + right) // 2
#     lefti, leftj, leftSubarrayMaxSum = MaxSumSubArrayDnC(left,mid,numbers)
#     righti, rightj, rightSubarrayMaxSum = MaxSumSubArrayDnC(mid+1,right,numbers)
#     # Conquer
#     centeri = mid
#     centerj = mid+1
#     leftsum = numbers[mid]
#     rightsum = numbers[mid+1]
#     leftmaxsum = numbers[mid]
#     rightmaxsum = numbers[mid + 1]
#     for i in range(mid-1, left-1,-1):
#         leftsum = leftsum+ numbers[i]
#         if leftsum > leftmaxsum:
#             leftmaxsum= leftsum
#             centeri=i
#     for j in range(mid+2, right+1):
#         rightsum = rightsum+ numbers[j]
#         if rightsum > rightmaxsum:
#             rightmaxsum= rightsum
#             centerj=j
#     centerSubarrayMaxSum = leftmaxsum + rightmaxsum
#
#     # Merging/Combining of sub problems solutions
#     if leftSubarrayMaxSum > rightSubarrayMaxSum:
#         if leftSubarrayMaxSum > centerSubarrayMaxSum:
#             return lefti, leftj, leftSubarrayMaxSum
#         else:
#             return centeri, centerj, centerSubarrayMaxSum
#     else:
#         if rightSubarrayMaxSum > centerSubarrayMaxSum:
#             return righti, rightj, rightSubarrayMaxSum
#         else:
#             return centeri, centerj, centerSubarrayMaxSum


# Calling the recursive method
# mssi, mssj, mss = MaxSumSubArrayDnC(0, lenOfNumbers-1, numbers)
# print("Max sum of Subarray: " + str(mss))
# print("Max Subarray: " + str(numbers[mssi:mssj+1]))

#O(n)

cs=numbers[0]
gs=numbers[0]
gsStart=0
gsEnd=0
csStart=0
csEnd=0
for i in range(1, lenOfNumbers):
    if(cs <= 0):
        csStart=i
        csEnd=i
        cs= numbers[i]
    else:
        cs=cs+numbers[i]
        csEnd=i
    if(cs >= gs ):
        gs=cs
        gsStart=csStart
        gsEnd=csEnd
print("Max subarray:"+ str (numbers[gsStart:gsEnd+1]))
print("Max subarray sum:" + str (gs))
