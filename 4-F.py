print("m stands for month")
print("d stands for day")
print("y stands for year")
print("Please Enter in the format of mm/dd/yyyy")

a = input("Enter the date : ")
s = a.split(sep='/')
#print(s)

def num_to_month(n):
    if (n == '1') | (n=="01"):
        return "January"
    elif (n == '2') | (n=="02"):
        return "february"
    elif (n == '3') | (n=="03"):
        return "March"
    elif (n == '4') | (n=="04"):
        return "April"
    elif (n == '5') | (n=="05"):
        return "May"
    elif  (n == '6') | (n=="06"):
        return "June"
    elif (n == '7') | (n=="07"):
        return "July"
    elif (n == '8') | (n=="08"):
        return "August"
    elif (n == '9') | (n=="09"):
        return "September"
    elif (n == '10') | (n=="10"):
        return "October"
    elif (n == '11') | (n=="11"):
        return "November"
    else:
        return "December"

print("{} {},{}".format(num_to_month(s[0]),s[1],s[2]))


