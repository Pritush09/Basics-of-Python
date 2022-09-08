first_list=[2,3,4,5,6,7,8]
second_list=[i**2 for i in first_list]
out = set([(i,i**2) for i in first_list])
print(out)