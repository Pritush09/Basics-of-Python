l = [1,2,3,4,5,6,7]
le = len(l)
print(le)
li = [0]
for i in range(1,le):
    try:
        li.append(l[i-1])
    except:
        pass
    if i==le-1:
        li[0]=l[le-1]
print(li)