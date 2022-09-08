d = {'jan':52,'feb':52,'march':52,'april':34,'may':76,'june':45,'july':22,'august':88,'sep':45}
#print(d.keys()[0])

print(d.keys())

print(d.values())
print(len(d.values()))

l = list(d.values())
print(l)
m = len(l)
n = []
for i in range(m):
    for j in range(i+1,m):
        if l[i]==l[j]:
            l[j] = 0

    if l[i]!=0:
        n.append(l[i])
print(n)