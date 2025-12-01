# Answer 1
print("\nAnswer 1")


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()

for _ in range(10):
    print(next(fib_gen))

# Answer 2
print("\nAnswer 2")


def infinite_multiples(a):
    i = 1
    while True:
        yield a * i
        i += 1


multiples = infinite_multiples(3)

for i in range(10):
    print(next(multiples))

# Answer 3
print("\nAnswer 3")


def repeat_word(word, times):
    for i in range(times):
        yield word


for w in repeat_word('Hello', 5):
    print(w)
