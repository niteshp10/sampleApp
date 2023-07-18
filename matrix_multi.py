import numpy as np
a = [[2,3,4],[1,2,3],[6,3,5],[9,2,1]]
b=[[4,5],[1,8],[0,5]]
c = [[0]*len(b[0]) for i in range(len(a))]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j] += a[i][k]*b[k][j]
print(c)

print(np.dot(a,b))