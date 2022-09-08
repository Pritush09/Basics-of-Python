first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
cnt = 0
for ele in first_set:
    for elem in second_set:
        if elem == ele:
            cnt += 1

if (cnt <= len(first_set)):
    print("First set is a subset of second set - True")
    print("Second set is a subset of second set - False")
    print("First set is a super set of second set - False")
    print("Second set is a super set of second set - True")
    first_set = set()
    print("First Set ", first_set)
    print("Second Set ", second_set)
