# Answer 1
print("\nAnswer 1")
strings = ["1", "2", "3", "4"]
integers = [int(word) for word in strings]
print(integers)

# Answer 2
print("\nAnswer 2")
numbers = [1, 5, 13, 4, 16, 7]
greater_than_10 = [num for num in numbers if num > 10]
print(greater_than_10)

# Answer 3
print("\nAnswer 3")
n = int(input("Enter a number: "))
squares = [(num + 1) * (num + 1) for num in range(n)]
print(squares)

# Answer 4
print("\nAnswer 4")
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
flattened_matrix = [element for sublist in matrix for element in sublist]
print(flattened_matrix)

# Answer 5
print("\nAnswer 5")
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
print(dictionary)

# Answer 6
print("\nAnswer 6")
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
score_above_80 = {k: v for k, v in scores.items() if v > 80}
print(score_above_80)
