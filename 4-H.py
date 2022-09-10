# to find the sum of each row of matix (m*n)
# one-liner logic to take input for rows and columns
#mat = [[int(input()) for x in range (C)] for y in range(R)]
matrix = [[1,2,3],[1,2,3]]
print(len(matrix[0]))
s=0

for i in range(len(matrix)):
    sd = s
    for j in range(len(matrix[i])):
        s = s + matrix[i][j]
    print(s-sd,end=" ")