ice_cream = ["vanella", "chocolate", "butterchoe", "buleberry"]
print(ice_cream[1])
print(ice_cream[-1])

ice_cream.append("bulebeey")
ice_cream.insert(1, "buleberry")
ice_cream.remove("chocolate")
ice_cream.pop()
print(len(ice_cream))

for item in ice_cream:
    print(item)

building = ("building1", "building2", "building3", "building3")
print(building[0])
print(building)

num = {1, 2, 3, 4, 5}
num.add(6)
num.remove(4)
print(num)

school = {
    'name': 'xyz School',
    'add': 'Bhubaneswar',
    'buildings': 6,
    'city': 'BBSR'
}
school_address = school['add']
school["students"] = 1000

for key, val in school.items():
    print(key, "-", val)

name = "Suraj is a student"
print(name.upper())
print(name.lower())

for char in name:
    print(char)
    
updated_name = name.replace("Suraj", "Sarita")    
print(updated_name)
