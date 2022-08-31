s = 1
n = int(input("Enter the range for n : "))
for i in range(2,n+1):
    if i%2==0:
        s= s-1/i
    elif i%2!=0:
        s=s+1/i
print("The sum of the series is {}".format(s))
