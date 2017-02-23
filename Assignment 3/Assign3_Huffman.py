# https://docs.python.org/2/library/heapq.html
# EXTRACT-MIN = heappop(heap)
from collections import *
import heapq
import sys
# Taken straight from Lecture 6 - Greedy Algorithms
'''
Huffman(C):
n = |C|
Q = C
for i = 1 to n-1
    create a new node z
    x = EXTRACT-MIN(Q)
    y = EXTRACT-MIN(Q)
    z.left = x
    z.right = y
    z.freq = x.freq + y.freq
    INSERT(Q,z)
end for
return EXTRACT-MIN(Q)
'''
'''
class Node(list):
    def __init__(self, left_node = None, right_node = None, root = None):
        self.left_node = left_node
        self.right_node = right_node
    def children(self):
        return ((self.left_node, self.right_node))
'''

def huffman(list):
    Q = list
    #for i in range(len(Q)):
    #    Q[i] += (" ",)
    heapq.heapify(Q)
    print "Frequency:  Symbol:\n------------"
    for i in range(len(Q)):
        print Q[i]
    while(len(Q) > 1):
        left, right = heapq.heappop(Q), heapq.heappop(Q)
        #node = Node(Q)
        parent = (left[0]+right[0], left, right)
        heapq.heappush(Q, parent)
    return Q[0]

def printHuffman(Q, prefix = ''):
    if(len(Q) == 2):
        print(Q[1], prefix)
    else:
        printHuffman(Q[1], prefix + '0')
        printHuffman(Q[2], prefix + '1')



#test = "the quick brown fox jumps over the lazy dog"
d = defaultdict(int)

#for i in test:
#    d[i] += 1
file_name = sys.argv[1]
f = open(file_name, "r")
data = f.read()
f.close()

for i in data:
    d[i] += 1
list = []
for char, freq in d.items():
    temp = freq, char
    list.append(temp)
#print list
#heapify(list)
#print list
#x = heappop(list)
#y = heappop(list)
#print x, y
hufflist = huffman(list)
print "\nSymbol: Prefix\n ------------"
printHuffman(hufflist)