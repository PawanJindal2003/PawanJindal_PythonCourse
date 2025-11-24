# Answer 1
print("\nAnswer 1")
num = int(input("Enter a number to check if it is odd/even: "))
if num % 2 == 0:
    print("It is an even number.")
else:
    print("It is an odd number.")

# Answer 2
print("\nAnswer 2")
words = ["civic", "hello"]
for word in words:
    reversedWord = word
    i = 0
    size = len(word)
    for c in word:
        reversedWord = reversedWord.replace(word[size - i - 1], word[i])
        i += 1
    if reversedWord == word:
        print("%s is a palindrome" % word)
    else:
        print("%s is not a palindrome" % word)

# Answer 3
print("\nAnswer 3")
num = int(input("How many fibonacci numbers do want ? "))
a = 0
b = 1
fiboList = [a]
for i in range(num):
    c = a + b
    fiboList.append(c)
    a = b
    b = c
print(fiboList)

# Answer 4
print("\nAnswer 4")
searchList = [1, 2, 3, 4, 5]
target = int(input("Enter the target sum: "))
searchList.sort()
i, j = 0, len(searchList) - 1
resultList = []
for _ in searchList:
    if i >= j:
        break
    s = searchList[i] + searchList[j]
    if s == target:
        resultList.append(searchList[i])
        resultList.append(searchList[j])
        break
    elif s > target:
        j -= 1
    else:
        i += 1
print(resultList)

# Answer 5
print("\nAnswer 5")
i = 0
while i <= 20:
    if i % 2 == 0:
        print(i, end=", ")
    else:
        i += 1
        continue
    i += 1

# Answer 6
print("\n\nAnswer 6")
searchList = [10, 20, 30, 40, 50]
for i in range(len(searchList)):
    if searchList[i] == 30:
        print("Number 30 found at index : %d, hence not searching further" % i)
        break

# Answer 7
print("\nAnswer 7")
i = 0
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i, end=", ")
    i += 1

# Answer 8
print("\nAnswer 8")
# Output:
# 0
# 1
# 2
# 3
# 4

# Answer 9
print("\nAnswer 9")
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
day = str(input("Enter a day : "))
day = day.lower()
for i in range(len(days)):
    if day == days[i]:
        if i == 5 or i == 6:
            print("It is a weekend")
        else:
            print("It is a weekday")
        break
