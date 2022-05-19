#function waits for user input. Default is string, can be type casted
print("Enter name: ")
name = input()
print("Enter age: ")
age = input()
print("Enter gender: ")
gender = input()
print("name: "+name+" age:"+age+" gender: "+gender)

#type casting inputs
print("Enter a number: ")
n1 = input()
print("Enter another number: ")
n2 = input()
print(n1 + n2)
print(int(n1) + int(n2))

print("Enter a number: ")
n1 = int(input())
print("Enter another number: ")
n2 = int(input())
print(n1 + n2)