# update()
# we can convert the tuple to a list and add item

dic = {}
l = [('Blue',4),('Red',0),('Red',1),('Black',1),('Yellow',9)]
for i in l:
    x,y=i
    if x in dic:
        dic[x] = dic[x]+[y]
    else:
        dic[x]=[y]

print(dic)
