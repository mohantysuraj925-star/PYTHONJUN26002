class Car:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

    def display_details(self):
        print(self.brand, self.color, self.model)

car1 = Car("Toyota", "Red", "Camry")
car2 = Car("Hyundai", "Black", "i20")
car1.display_details()
car2.display_details()


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def displayStudent(self):
        print(self.name, self.age, self.course)

student1 = Student("Rahul", 14, "Computer Science")
student1.displayStudent()


class Employee:
    def __init__(self, employee_name, employee_id, salary):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(self.employee_name, self.employee_id, self.salary)

emp1 = Employee("Amit", "EMP101", 50000)
emp2 = Employee("Priya", "EMP102", 60000)
emp3 = Employee("Vikram", "EMP103", 55000)
emp1.display_details()
emp2.display_details()
emp3.display_details()


class Mobile:
    def __init__(self, brand, RAM, storage, price):
        self.brand = brand
        self.RAM = RAM
        self.storage = storage
        self.price = price

    def display_info(self):
        print(self.brand, self.RAM, self.storage, self.price)

phone1 = Mobile("Vivo", "8GB", "128GB", 15000)
phone1.display_info()


class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def display_details(self):
        print(self.account_holder_name, self.account_number, self.balance)

account1 = BankAccount("Suraj Kumar Mohanty", "9876543210", 25000)
account1.display_details()


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def displayBook(self):
        print(self.title, self.author, self.price)

book1 = Book("Python Basics", "John", 450)
book1.displayBook()


class Building:
    def __init__(self):
        self.building_name = input("Enter building name: ")
        self.location = input("Enter location: ")
        self.number_of_floors = input("Enter floors: ")

    def display_info(self):
        print(self.building_name, self.location, self.number_of_floors)


class Citizen:
    country = "India"

    def __init__(self, aadhar, phone, name):
        self.aadhar = aadhar
        self.phone = phone
        self.name = name

    def print_details(self):
        print(self.name, self.aadhar, self.phone, self.country)

citizen1 = Citizen("[Aadhaar Redacted]", "91182912829", "Suraj")
citizen1.print_details()


class Laptop:
    def __init__(self, brand, processor, RAM, price):
        self.brand = brand
        self.processor = processor
        self.RAM = RAM
        self.price = price

    def display_details(self):
        print(self.brand, self.processor, self.RAM, self.price)

lap1 = Laptop("HP", "Intel i5", "16GB", 55000)
lap2 = Laptop("Dell", "Ryzen 5", "8GB", 48000)
lap3 = Laptop("Lenovo", "Intel i7", "16GB", 75000)
lap1.display_details()
lap2.display_details()
lap3.display_details()


class Movie:
    def __init__(self, movie_name, hero_name, release_year):
        self.movie_name = movie_name
        self.hero_name = hero_name
        self.release_year = release_year

    def display_method(self):
        print(self.movie_name, self.hero_name, self.release_year)

movie1 = Movie("KGF", "Yash", 2018)
movie1.display_method()


class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    def print_info(self):
        print(self.name, self.subject, self.experience)

teacher1 = Teacher("Dr. Mishra", "Python", 10)
teacher1.print_info()


class Hospital:
    def __init__(self, hospital_name, doctor_count, city):
        self.hospital_name = hospital_name
        self.doctor_count = doctor_count
        self.city = city

    def display_method(self):
        print(self.hospital_name, self.doctor_count, self.city)

hosp1 = Hospital("AIIMS", 150, "Bhubaneswar")
hosp1.display_method()


class Product:
    def __init__(self, product_name, category, price):
        self.product_name = product_name
        self.category = category
        self.price = price

    def display_details(self):
        print(self.product_name, self.category, self.price)

prod1 = Product("Mouse", "Electronics", 500)
prod2 = Product("Keyboard", "Electronics", 1200)
prod3 = Product("Monitor", "Electronics", 8500)
prod1.display_details()
prod2.display_details()
prod3.display_details()
