def say_hi():
    print("Hi there!")
say_hi()

def print_my_name():
    print("My name is Phenix Payton!")
print_my_name()

def draw_box():
    print("+-----+")
    print("|     |")
    print("+-----+")

draw_box()


def print_star():
    print("*")
# Add your code here to call it twice
print_star()
print_star()


def greet(name):
    print(f"Hello, {name}!")
# Call it here with your name
greet("Phenix")

# Define function here
# Call it with 5
def double(n):
    product = n *2
    print(f"double {n} is {product}")

double(5)

def introduce(first_name, last_name, age):
    print(f"Hello, I'm {first_name} {last_name} and I'm {age} years old.")

introduce("Phenix","Payton",23)

def add_five(n):
    answer = n + 5
    return answer
# Add return here
result = add_five(10)
print(result) # Should print 15

def is_even(n):
    if n % 2 == 0:
        return True
    return False

print(is_even(4)) # Should print True
print(is_even(7)) # Should print False

def calculate_average(a, b):
    total = a + b
    average = total / 2
    return average
result = calculate_average(10, 20)
print(f"Average is {result}")