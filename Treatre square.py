import math

l=list(map(int,input().strip().split()))
n=l[0]
m=l[1]
a=l[2]

M = math.ceil(m/a)
A = math.ceil(n/a)

print(M * A)

