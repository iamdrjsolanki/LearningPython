xyz = "Welcome to"
abc = "Python"
num = 3 #int
year = 2.022 #float
print(type(xyz))
print(xyz)
print(xyz + " " + abc)
#throws error cannot concate int after str
#print(xyz + " " + abc + " "+ num)
print(xyz + " " + abc + " {} in year {}".format(num, year))
print(xyz[0])
#slicing
print(xyz[0:7])
#negative slicing
print(xyz[-6:])
print(xyz[-6:-2])
print(len(xyz))
print(len(xyz+abc))
a = "   HI  World how are you    "
print(len(a))
print(len(a.strip()))
print(a.lower())
print(a.strip().upper())
print(a.find("a"))
print(a.find("are"))
print(a.find("z"))
print(a.find("bar"))
b = "HI World how are you"
print(b.split(" "))

#list - creates a 2D array
alist = ["apple", "banana", "chickoo"]
print(alist)
print(alist[2])
print(alist[2][0])
print(alist[2][0:3])
#get index & modify index
alist[alist.index("banana")] = "strawberry"
print(alist)
if "banana" in alist:
    print("yes")
else:
    print("no")

alist.append("banana")
print(alist)
alist.remove("chickoo")
#gives error if not in list
#alist.remove("mango")
print(alist)
alist.reverse()
print(alist)
blist = ["mango", "grapes"]
print(alist + blist)
#puts all items in 2nd list to 1st list
alist.extend(blist)
print(alist)

#tuple
#in list [] is used, in tuple () is used to create
#tuple is unchangeable/immutable
atup = ("apple", "banana", "chickoo")
print(atup)

print(alist[2])
print(alist[2][0])
print(alist[2][0:3])
#get index & modify index
alist[alist.index("banana")] = "strawberry"
print(alist)
if "banana" in alist:
    print("yes")
else:
    print("no")

alist.append("banana")
print(alist)

#dictionary - dict
adict = {}
print(type(adict))
adict["name"] = "Dhiraj"
adict["age"] = 29
print(adict)
bdict = {'name': 'Dhiraj', 'age': 29, 'gender': 'Male'}
print(bdict)
bdict.pop("gender")
print(bdict)
bdict['gender'] = 'Male'
bdict.popitem()
print(bdict)
bdict1 = {'name': 'Dhiraj1', 'age': 29, 'gender': 'Male'}
bdict2 = {'name': 'Dhiraj2', 'age': 29, 'gender': 'Male'}
bdict3 = {'name': 'Dhiraj3', 'age': 29, 'gender': 'Male'}
bdict4 = {'name': 'Dhiraj4', 'age': 29, 'gender': 'Male'}
bdictNested = {
    'emp1': bdict1,
    'emp2': bdict2,
    'emp3': bdict3,
    'emp4': bdict4
}
print(bdictNested)