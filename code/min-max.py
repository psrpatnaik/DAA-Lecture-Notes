import random
import time
numbers = random.sample(range(0, 10000000), 500000)
#print(numbers)

lenOfNumbers= len(numbers)
minNumber = 0
maxNumber = 0


if(numbers[0] < numbers[1]):
    minNumber = numbers[0]
    maxNumber = numbers[1]
else:
    minNumber = numbers[1]
    maxNumber =  numbers[0]

i = 2

t1=time.time()
# create a window of size 2 and keep moving it till the end of the array
while(i < lenOfNumbers -1 ):
    if(numbers[i] < numbers[i+1]):
        if(minNumber > numbers[i]):
            minNumber= numbers[i]
        if(maxNumber < numbers[i+1]):
            maxNumber = numbers[i+1]
    else:
        if (minNumber > numbers[i+1]):
            minNumber = numbers[i+1]
        if (maxNumber < numbers[i]):
            maxNumber = numbers[i]
    i+=2
t2=time.time()

# print("minimum number " + str(minNumber))
# print("maximum number "+ str(maxNumber))
print("Time required (Pairwise)"+ str(t2-t1))
# print(min(numbers))
# print(max(numbers))


def minmax(numbers,left, right):
    # subproblem of size 1
    if(left == right):
        return numbers[left], numbers[left]
    # subproblem of size 2
    if(left == right -1):
        if(numbers[left] < numbers[right]):
            return numbers[left], numbers[right]
        else:
            return numbers[right], numbers[left]
    # subproblem of size > 2
    minFirstHalf, maxFirstHalf = minmax(numbers, left, ((left + right)//2))
    minSecondHalf, maxSecondHalf = minmax(numbers, (((left + right) // 2) +1), right)

    # merging solutions of two subproblems
    minToReturn = minFirstHalf if minFirstHalf < minSecondHalf else minSecondHalf
    maxToReturn = maxFirstHalf if maxFirstHalf > maxSecondHalf else maxSecondHalf

    return minToReturn, maxToReturn
# call to method
t3=time.time()
minDnC, maxDnC = minmax(numbers,0,lenOfNumbers-1)
t4=time.time()

# print("minimum number (DnC) " + str(minDnC))
# print("maximum number (DnC) " + str(maxDnC))
#
# print("minimum number (min method) " + str(min(numbers)))
# print("minimum number (max method) " + str(max(numbers)))
print("Time required (DnC)" + str(t4-t3))

# Comparisions 3n/2 -2
