inm = int(input("Enter the number of rows : "))
nm = 1
for i in range(1,inm+1):
    for j in range(1,i+1):
        print(nm,end=' ')
        nm = nm+1
    print()