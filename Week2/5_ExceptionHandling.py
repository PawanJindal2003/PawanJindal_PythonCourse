# Answer 1
print('\nAnswer 1')
a, b = 10, 0
try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Handling zero division method")

# Answer 2
print('\nAnswer 2')
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Handling out of range error")

# Answer 3
print('\nAnswer 3')


def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both values must be numbers.")


safe_divide(1, 0)
safe_divide(1, "a")
