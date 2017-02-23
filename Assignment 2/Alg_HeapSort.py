__author__ = 'Adam Lieu (100451790)'
import math

# Root of tree = a[0]
# parent of a[i] = a[floor(i/2)]
# left child of a[i] = a[2i]
# right child of a[i] = a[2i + 1]
# [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
# [16,14,10,8,7,9,3,2,4,1]
# 14 = a[0+1]
# 10 = a[0+2]


#Takes an almost-heap with one violation and fixes the violation
# Lecture 3, slide 6
#def max_heapify(array, index):
def max_heapify(array, index, n):
    left_child = 2*index+1
    right_child = 2*index+2
    maximum = index
    if left_child < n and array[left_child] > array[maximum]:
        maximum = left_child
    if right_child < n and array[right_child] > array[maximum]:
        maximum = right_child
    if maximum != index:
        temp = array[index]
        array[index] = array[maximum]
        array[maximum] = temp
        max_heapify(array, maximum, n)


# Takes an arbitrary array and builds it into a max heap
# Lecture 3, slide 14
def build_max_heap(array, n):
    length = len(array)
    for i in range(int(math.floor(length/2)), -1, -1):
        max_heapify(array, i, n)


# Returns the largest element in the max heap
def heap_maximum(array):
    return array[0]


# Removes and returns the largest elemet in the max heap
# Lecture 3, slide 21
def heap_extract_max(array):
    if len(array) < 1:
        print "error: heap underfow"
        return 0
    maximum = array[0]
    max_length = len(array)
    array[0] = array[max_length-1]
    #max_length -= 1
    max_heapify(array, 1, len(array))
    return maximum


# Inserts a new element into the heap, preserving the heap property
# Lecture 3, slide 24
def max_heap_insert(array, x):
    length = len(array) + 1
    array.insert(length, x)
    #print array
    i = len(array) - 1
    while array[i] > array[int(math.floor(i/2))] and i > 0:
        #print i
        temp = array[i]
        array[i] = array[int(math.floor(i/2))]
        array[int(math.floor(i/2))] = temp
        i = int(math.floor(i/2))


def heapsort(array, n):
    build_max_heap(array, len(array))
    length = len(array)-1
    for i in range(length, -1, -1):
        # print i
        temp = array[0]
        array[0] = array[i]
        array[i] = temp
        max_heapify(array, 0, i)


def printAsTree(array, root):
    print createSidewaysTree(array, root, 0)


def createSidewaysTree(array, root, depth):
    left_child = 2*root + 1
    right_child = 2*root + 2
    sideways_tree = ""
    if right_child < len(array):
        sideways_tree += createSidewaysTree(array, right_child, depth+1)

    sideways_tree += "\n" + (depth*"\t") + str(array[root])

    if left_child < len(array):
        sideways_tree += createSidewaysTree(array, left_child, depth+1)

    return sideways_tree


def printAsArray(array):
    print array


array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print "Array is: \t", array
print "Building array into max heap."
build_max_heap(array, len(array))
printAsArray(array)
printAsTree(array, 0)
print "Maximum of heap is:\t", heap_maximum(array)
print "Heap extract max:\t", heap_extract_max(array)

max_heap_insert(array, 20)
print "Max_heap_insert: ", printAsArray(array)
printAsTree(array, 0)
heapsort(array, len(array))
print "Heapsort:\t", array

