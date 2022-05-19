count = 1
while count <= 10:
    print(count)
    count += 1

print("Enter a response as yes or no:")
userRes = input()
while userRes == "yes":
    print("Enter a number:")
    n1 = int(input())
    print("Enter a number:")
    n2 = int(input())
    result = n1 + n2
    print("The result: {}".format(result))
    print("Enter a response as yes or no:")
    userRes = input()
if(userRes == "no"):
    print("exiting....")


for number in range(10):
    print(number)

for number in range(1, 10):
    print(number)

for number in range(1, 10, 2):
    print(number)
for number in range(2, 10, 2):
    print(number)

str = "asdafdgasd"
for character in str:
    print("character: "+character)

alist = ["apple", "banana", "chickoo"]
for fruit in alist:
    print("fruit: "+fruit)
for i, fruit in enumerate(alist):
    print("index: {}".format(i) + " fruit: "+fruit)

atup = ("apple", "banana", "chickoo")
for fruit in atup:
    print("fruit: "+fruit)
for i, fruit in enumerate(atup):
    print("index: {}".format(i) + " fruit: "+fruit)


