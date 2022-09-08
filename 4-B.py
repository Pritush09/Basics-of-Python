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


#for i in li:
#    dic[i] = 0
#for i in li:
#    dic[i] = dic[i] + 1
#
#for i, j in dic.items():
 #   print("No. %d is present %d times" % (i, j))
