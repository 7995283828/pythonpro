num= int(input("Enter any number: "))
flag = num%2
if flag == 0:
    print(num, "is an Even number")
elif flag == 1:
    print(num, "is an Odd number")
else:
    print("Error, invalid input")
