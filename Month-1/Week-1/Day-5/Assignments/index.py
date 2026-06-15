full_name = "Suraj Kumar Mohanty"
print(full_name)

user_str1 = "Bhubaneswar"
print(len(user_str1))

user_str2 = "Python"
print(user_str2.upper())
print(user_str2.lower())

text_slice = "Python Programming"
print(text_slice[0:6])
print(text_slice[7:18])
print(text_slice[-5:])

sentence = "banana"
print(sentence.count("a"))

java_str = "I love Java Programming"
print(java_str.replace("Java", "Python"))

rev_str = "Hacking"
print(rev_str[::-1])

pal_str = "madam"
if pal_str == pal_str[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print(fruits)

num_list = [1, 2, 3]
num_list.append(4)
num_list.insert(1, 10)
print(num_list)

colors = ["Red", "Green", "Blue"]
colors.remove("Green")
print(colors)

mix_nums = [4, 15, 8, 42, 2]
print(max(mix_nums))
print(min(mix_nums))
print(sum(mix_nums))

numbers_filter = [10, 15, 20, 25, 30, 35, 40]
for num in numbers_filter:
    if num % 2 == 0:
        print(num)

count_list = [1, 2, 3, 4, 5]
total_elements = 0
for element in count_list:
    total_elements += 1
print(total_elements)

cities = ("Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore")
print(cities)
print(cities[0])
print(cities[-1])

occ_tuple = (1, 2, 3, 2, 4, 2, 5)
print(occ_tuple.count(2))

convert_tuple = (10, 20, 30)
convert_list = list(convert_tuple)
print(convert_list)

unique_set = {10, 20, 30, 40, 50}
print(unique_set)

dup_list = [1, 2, 2, 3, 4, 4, 5, 5]
conv_set = set(dup_list)
print(conv_set)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))

op_set = {1, 2, 3}
op_set.add(4)
op_set.remove(2)
print(op_set)

student_info = {
    "name": "John",
    "age": 22,
    "course": "Python",
    "city": "Mumbai"
}
print(student_info.values())

student_info["age"] = 23
student_info["email"] = "john@example.com"
print(student_info.keys())
print(student_info.values())

for key, value in student_info.items():
    print(key, ":", value)

employee = {
    "employee_id": "EMP101",
    "employee_name": "Rahul",
    "salary": 50000,
    "department": "IT"
}
print(f"ID: {employee['employee_id']}, Name: {employee['employee_name']}, Salary: {employee['salary']}, Dept: {employee['department']}")

marks = {"Math": 85, "Science": 90, "English": 78}
total_marks = sum(marks.values())
avg_marks = total_marks / len(marks)
print(total_marks)
print(avg_marks)

word_sentence = "Python is awesome"
words = word_sentence.split()
print(len(words))

input_word = "programming"
unique_chars = ""
for char in input_word:
    if char not in unique_chars:
        unique_chars += char
print(unique_chars)

keys = ["name", "age", "city"]
values = ["John", 22, "Mumbai"]
combined_dict = dict(zip(keys, values))
print(combined_dict)

students_dict = {}
students_dict["1"] = {"name": "Suraj", "course": "Python"}
print(students_dict)
