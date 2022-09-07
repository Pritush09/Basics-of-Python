# https://stackoverflow.com/questions/5518435/python-fastest-way-to-create-a-list-of-n-lists

m = [1,2,3,4,5,6,7,8,9]
sm = list(reversed(m))
print(sm)

if len(m)%3!=0:
    print("The list cannot be converted into 3 equal chunks")

elif len(m)%3 == 0:
    n = len(m)//3
    print(n)
    l = [[] for i in range(0,n)]
    print(l)
    s = 0
    b = 0
    for i in range(n):
        for j in range(0,3):
            l[i].append(m[s])
            s+=1
        l[i] = list(reversed(l[i]))
        i += 1

print(l)