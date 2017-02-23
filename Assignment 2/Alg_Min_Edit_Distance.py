"""
Initialization:
D(i, 0) = i
D(0, j) = j
Recurrence relation:
For each i = 1..M
    For each j = 1..N
        D(i,j) = min(D(i-1,j)+1,
                    D(i,j-1)+1,
                    D(i-1,j-1)+...
                        2 (if x(i) != y(j))
                        0 (if x(i) = y(j))
Termination:
D(n, m) is distance

Two strings:
X of length n
Y of length m
Edit distance between x and y: D(n,m)
"""


def minEditDistance(word_x, word_y):
    n = len(word_x)
    m = len(word_y)
    #print n, m

    dist = [[0 for i in range(m + 1)] for j in range(n + 1)]
    #print dist
    for i in range(1, n+1):
        for j in range(1, m+1):
            #print i-1, j-1
            if word_x[i-1] != word_y[j-1]:
                temp3 = 2
            elif word_x[i-1] == word_y[j-1]:
                temp3 = 0
            dist[i][0] = i
            dist[0][j] = j
            dist[i][j] = min(dist[i-1][j] + 1,
                             dist[i][j-1] + 1,
                             dist[i-1][j-1] + temp3)
    #print dist
    return dist[n][m]

print "Distance of spoof and stool: "
print minEditDistance("spoof", "stool")
print "Distance of podiatrist and pediatrician: "
print minEditDistance("podiatrist", "pediatrician")
print "Distance of blaming and conning: "
print minEditDistance("blaming", "conning")