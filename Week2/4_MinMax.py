# Answer 1
print('\nAnswer 1')
numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
print(min(numbers), max(numbers))

# Answer 2
print('\nAnswer 2')
setn = {5, 10, 3, 15, 2, 20}
print(min(setn), max(setn))

# Answer 3
print('\nAnswer 3')
words = ["apple", "banana", "kiwi", "grapefruit", "orange"]


def shortest_longest_word(words):
    min_word = words[0]
    max_word = words[0]

    for word in words:
        if len(word) < len(min_word):
            min_word = word
        if len(word) > len(max_word):
            max_word = word
    return min_word, max_word


print(shortest_longest_word(words))
