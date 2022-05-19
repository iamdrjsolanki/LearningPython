print("Enter a number: ")
n1 = input()

if(n1.isnumeric() and int(n1) > 0):
    print("Enter another number: ")
    n2 = input()
    if(n2.isnumeric() and int(n2) > 0):
        print("Divison of the number is: ")
        print(int(n1) / int(n2))
    else:
        print("Second input is not numeric or zero")
else:
    print("First input is not numeric or zero")


