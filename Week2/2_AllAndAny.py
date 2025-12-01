# Answer 1
print("\nAnswer 1")
a = [1, 2, 3, 4, 5]
isPositive = all(x > 0 for x in a)
print(isPositive)

# Answer 2
print("\nAnswer 2")
a = [1, 3, 5, 7, 8]
hasEven = any(x % 2 == 0 for x in a)
print(hasEven)

# Answer 3
print("\nAnswer 3")
a = [1, 3, 5, 7, 8]
divisible_by_5 = any(x % 5 == 0 for x in a)
print(divisible_by_5)
