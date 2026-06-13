def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def calculate_area(length, width):
    return length * width

global_var = "Global Value"

def show_scope():
    local_var = "Local Value"
    print("Global inside function:", global_var)
    print("Local inside function:", local_var)

def outer_function():
    outer_var = "Outer Value"
    
    def inner_function():
        print("Nested output:", outer_var)
        
    inner_function()

print("Result 1:", check_even_odd(8))
print("Result 2:", calculate_area(6, 12))
show_scope()
outer_function()
