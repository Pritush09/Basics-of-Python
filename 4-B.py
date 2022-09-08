m = ['M','N','E','E','E','B','F']
n = len(m)
print(n)
d = {}
from collections import Counter
df = Counter(m)
for i in range(0,n):
    f = df[m[i]]
    d[m[i]] = f
    i+=1
print(d)

# https://www.geeksforgeeks.org/python-count-occurrences-element-list/