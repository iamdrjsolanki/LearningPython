import datetime

today1 = datetime.datetime.now()
print(today1)

today2 = datetime.datetime.today()
print(today2)

print(datetime.datetime.today().strftime("%d%m%y"))

print(datetime.datetime.today().strftime("%d-%m-%Y"))

print(datetime.datetime.today().strftime("%d-%m-%Y"))

today2 = datetime.datetime.today() - datetime.timedelta(days=3)
print(today2)

today2 = datetime.datetime.today() + datetime.timedelta(days=3)
print(today2)



