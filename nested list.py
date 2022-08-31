l = []
m = []
for i in range(int(input())):
    name = input()
    score = float(input())
    k =[name,score]
    l.append(k)
    m.append(score)
x = sorted(set(m))[1]
for n,s in sorted(l):
    if s == x:
        print(n)     