N = int(input())
l =[]
for i in range(N):
    s = input().split()
    for i in range(1,len(s)):#1,2 wala ko change kar rahe he int me
        s[i]= int(s[i])
    if s[0] == "append":
        l.append(s[1])
    elif s[0] == "sort":
        l.sort()
    elif s[0] == "insert":
        l.insert(s[1],s[2])
    elif s[0] == "pop":
        l.pop()
    elif s[0] == "remove":
        l.remove(s[1])
    elif s[0] == "reverse":
        l.reverse()
    elif s[0] == "print":
        print(l)