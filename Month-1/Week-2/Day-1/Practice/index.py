class Car:
    cat = "SUV"
    colo = "red"
    wheel = 4


car1 = Car()
car2 = Car()
car3 = Car()
car4 = Car()

print(car1.cat)
print(car1.colo)


class Student:
    name = "Rahul"
    age = 14

    def studentDetails(self):
        print("Student name is", self.name, "Age is", self.age)

    def viewInput(self, address, roll):
        print("This is the address", address, "This is roll", roll)


s1 = Student()
s1.studentDetails()
s1.viewInput("Bhubaneswar", 40)
print(s1.age)


class Citizen:

    def __init__(self, aadhar, phone, name):
        self.aadhar = aadhar
        self.phone = phone
        self.name = name

    def printCitizen(self):
        print("Aadhar -", self.aadhar)
        print("Phone -", self.phone)
        print("Name -", self.name)


c1 = Citizen("[Aadhaar Redacted]", "91182912829", "Suraj")
c1.printCitizen()


class Building:
    country = "India"

    def __init__(self):
        self.location = input("Enter Location : ")
        self.pin = input("Enter pincode : ")
        self.floor = input("Enter floor count : ")
        self.roomsInFloor = input("Enter room in each floor : ")

        print("Country -", self.country)
        print("Location -", self.location)
        print("Pin -", self.pin)
        print("Floor -", self.floor)
        print("Rooms In Floor -", self.roomsInFloor)


building1 = Building()
