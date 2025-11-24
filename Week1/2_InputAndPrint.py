# Answer 1
print("\nAnswer 1")
name = str(input("Enter your name : "))
print("Hello " + name)

# Answer 2
print("\nAnswer 2")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print("Addition : %d" % (num1 + num2))
print("Subtraction : %d" % (num1 - num2))
print("Multiplication : %d" % (num1 * num2))
print("Division : %f" % (num1 / num2))

# Answer 3
print("\nAnswer 3")
name = str(input("Enter your full name in coma separated manner : "))
nameList = name.replace(" ", "").split(",")
print(nameList)

# Answer 4
print("\nAnswer 4")
age = int(input("Enter your age : "))
if age < 18:
    print("You are not eligible to vote.")
else:
    print("You are eligible to vote.")

# Answer 5
print("\nAnswer 5")
pi = 3.14159
print(f"{pi:.2f}")
