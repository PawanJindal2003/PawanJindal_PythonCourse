# Answer 1
print("\nAnswer 1")
def calculate_area(a, b=10):
    return a * b


print(calculate_area(3))


# Answer 2
print("\nAnswer 2")
def factorial(n):
    if n == 0:
        return 1
    return n * n - 1


print(factorial(5))


# Answer 3
print("\nAnswer 3")
def reverse_word(word):
    word = list(word)
    i, j = 0, len(word) - 1
    while i < j:
        word[i], word[j] = word[j], word[i]
        i += 1
        j -= 1
    return "".join(word)


print(reverse_word("Pawan"))


# Answer 4
print("\nAnswer 4")
def calculate_sum(a, b):
    s1, s2 = 0, 0
    for i in range(len(a)):
        s1 += a[i]
    for i in range(len(b)):
        s2 += b[i]
    return s1, s2


a = [8, 2, 3, 0, 7]
b = [3, -2, 5, 1]
print(calculate_sum(a, b))


# Answer 5
print("\nAnswer 5")
def distinct_sorted_list(a):
    a.sort()
    b = []
    for num in a:
        if len(b) == 0 or b[-1] != num:
            b.append(num)
    return b


a = [4, 1, 2, 3, 3, 1, 3, 4, 5, 1, 7]
print(distinct_sorted_list(a))
