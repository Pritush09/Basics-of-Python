n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
if query_name in student_marks:
    list_of = student_marks[query_name]
    a=0
    for i in list_of:
        a+=i
    b = a/len(list_of)
    print("{:.2f}".format(b))