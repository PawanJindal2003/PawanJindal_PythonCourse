# Answer 1
print("\nAnswer 1")
fruits = ["apple", "banana", "cherry"]
for a, fruit in enumerate(fruits):
    print(a, fruit)

# Answer 2
print("\nAnswer 2")
person = {"name": "Alice", "age": 30, "city": "New York"}
for i, (k, v) in enumerate(person.items()):
    print(k, ":", v)

# Answer 3
print("\nAnswer 3")
fruits_list = ["apple", "banana", "cherry", "date", "elderberry"]
fruits_tuple_list = []
for i, fruit in enumerate(fruits_list, start=1):
    if i % 2 == 0:
        fruits_tuple_list.append((i, fruit))
print(fruits_tuple_list)
