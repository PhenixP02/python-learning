def function_c():
    print(" Entering function C")
    print(" ...Leaving function C")
def function_b():
    print(" Entering function B")
    function_c() # A new "plate" for C is added
    print(" ...Leaving function B")
def function_a():
    print("Entering function A")
    function_b() # A new "plate" for B is added
    print("...Leaving function A")

function_a() # The first "plate" is added

def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(3)
# How many functions are on stack at deepest point?


def test():
    x = 5
    print(x)
test()
# Uncomment next line - what happens?
#print(x)


x = "global"
def outer():
    x = "outer"
    def inner():
        print(x)
    inner()
outer() # What prints and why?


count = 1
def update_counter():
    count = 10 # This shadows the global count
    print(f"Local count: {count}")
update_counter()
print(f"Global count: {count}")


x = 10
def change_x():
    global x
    x = 20
    print(f"New x: {x}")
change_x()


balance = 1000
def withdraw(amount):
    global balance
    balance -= amount
    pass
withdraw(100)
print(balance) # Should be 900

count = 0
def increment(num):
    count += num
    return(count)
increment(1)
print(count)
# Rewrite without global keyword
# Hint: Use parameter and return