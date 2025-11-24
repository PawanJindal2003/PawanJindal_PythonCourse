# Answer 1
print("\nAnswer 1")
nums = [1, 2, 3, 4, 5]
nums.sort()
print("Minimum : %d" % nums[0])
print("Maximum : %d" % nums[len(nums) - 1])

# Answer 2
print("\nAnswer 2")
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(a + b)

# Answer 3
print("\nAnswer 3")
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
freq = 0
for num in a:
    if num == 3:
        freq += 1
    else:
        continue
print(freq)

# Answer 4
print("\nAnswer 4")
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
a.sort()
print(a)

# Answer 5
print("\nAnswer 5")
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(numbers)

# Answer 6
print("\nAnswer 6")
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print(numbers)

# Answer 7
print("\nAnswer 7")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2))

# Answer 8
print("\nAnswer 8")
fruits = ("apple", "banana", "apple", "cherry")
freq = 0
for fruit in fruits:
    if fruit == "apple":
        freq += 1
    else:
        continue
print(freq)

# Answer 9
print("\nAnswer 9")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)

# Answer 10
print("\nAnswer 10")
dictionary = {"name": "Alice", "age": 30, "city": "New York"}
print(dictionary.get("age"))

# Answer 11
print("\nAnswer 11")
dictionary = {"name": "Alice", "age": 30, "city": "New York"}
dictionary["gender"] = "M"
print(dictionary)

# Answer 12
print("\nAnswer 12")
dictionary = {"name": "Alice", "age": 30, "city": "New York"}
dictionary.pop("city")
print(dictionary)

# Answer 13
print("\nAnswer 13")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(dict1 | dict2)
