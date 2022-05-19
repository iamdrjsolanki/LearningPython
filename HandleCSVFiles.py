filename = "username.csv"

with open(filename) as file_object:
    lines = file_object.readlines()

usernames = []

for i in lines:
    username = i.split(";")
    print(username[0])
    username.append(username)