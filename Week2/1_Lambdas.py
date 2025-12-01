from functools import reduce

# Answer 1
print("\nAnswer 1")
a = [1, 2, 3, 4]
double_a = list(map(lambda x: x * 2, a))
print(double_a)

# Answer 2
print("\nAnswer 2")
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double_a = list(filter(lambda x: x % 2 == 0, b))
print(double_a)

# Answer 3
print("\nAnswer 3")
words = ["apple", "banana", "cherry", "date"]
longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest_word)

# Answer 4
print("\nAnswer 4")
nums = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4, 59]
square_to_nearest_once = list(map(lambda x: round(x * x, 1), nums))
print(square_to_nearest_once)

# Answer 5
print("\nAnswer 5")
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
large_names = list(filter(lambda x: len(x) > 7, my_names))
print(large_names)

# Answer 6
print("\nAnswer 6")
sum_list = [1, 2, 3, 4, 5]
res = reduce(lambda x, y: x + y, sum_list)
print(res)
