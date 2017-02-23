from math import log10

def getdigit(num, digit):
    #print num, digit
    #return (num / (10**digit-1)) % 10
    return (num / (10**digit)) % 10
'''
# Input: A[1 .. n] (Arr in this case)
# Requires: A[j] in {0, 1, ... k}
# Output a sorted array B[1 .. n]
# Uses auxiliary storage: C[0 .. k]
def countingsort(array, k, exp):
    #Partially ripped from lecture slides
    b_array = [0] * len(array)
    c_array = [0] * 10
    n = len(array)

    #Initializes the counting array C
    # for i in range(0, k + 1):
    #for i in range(0, n):
    #    c_array[i] = 0

    #Counts the frequency of each possible values {0, ..., k}
    for j in range(0, n):
        digit = getdigit(array[j], k)
        c_array[array[j]] += 1

    #Computes the cumulative frequency
    for i in range(1, k + 1):
        c_array[i] += c_array[i - 1]

    #Outputs the values to the sorted array B
    for j in range(n - 1, 0 - 1, -1):
        b_array[c_array[(array[j]] - 1] = array[j]
        c_array[(array[j]] -= 1

    return b_array
'''

def radixsort(array):
    m = int(log10(max(array)) + 1)
    b_array = [0] * len(array)

    #Initializes the counting array C
    for j in range(m):
        c_array = [0] * 10

    #Counts the frequency of each possible values {0, ..., k}
        for i in array:
            digit = getdigit(i, j)
            #print digit
            c_array[digit] += 1

    #Computes the cumulative frequency
        for i in range(1, len(c_array)):
            c_array[i] = c_array[i] + c_array[i-1]

    #Outputs the values to the sorted array B
        for i in reversed(array):
            digit = getdigit(i, j)
            c_array[digit] -= 1
            new_dig = c_array[digit]
            b_array[new_dig] = i

        array = list(b_array)
        print array

    return b_array



radixarray = [326, 453, 608, 835, 751, 435, 704, 690]

#print getdigit(326, 0)
print radixsort(radixarray)