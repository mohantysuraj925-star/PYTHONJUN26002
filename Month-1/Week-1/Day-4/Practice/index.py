def welcome():
    print("Welcome to Python Programming")

def city(city_name):
    print("Welcome to", city_name)

def employee(name, department):
    print("Employee Name:", name)
    print("Department:", department)

def multiply(a, b):
    return a * b

def find_square(number):
    return number * number

def full_name(first_name, last_name):
    return first_name + " " + last_name

def student():
    student_name = "Rahul"
    print(student_name)

company = "Qlith Innovation"

def show_company():
    print(company)

def product_details():
    product_name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    print("Product:", product_name)
    print("Price:", price)

def calculate_discount(price):
    return price * 0.10

welcome()
print("-" * 20)

city("Mumbai")
print("-" * 20)

employee("Rahul", "IT")
print("-" * 20)

result = multiply(5, 4)
print("Result:", result)
print("-" * 20)

answer = find_square(6)
print("Square:", answer)
print("-" * 20)

name = full_name("Prakash", "Jena")
print(name)
print("-" * 20)

student()
print("-" * 20)

show_company()
print(company)
print("-" * 20)

amount = calculate_discount(5000)
print("Discount:", amount)
print("-" * 20)

product_details()
