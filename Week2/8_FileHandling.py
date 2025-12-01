# Answer 1
import csv

print('\nAnswer 1')
file_path = 'FilesForFileHandling/sample.txt'
with open(file_path, 'r') as file:
    file_content = file.read()
print(file_content)

# Answer 2
print('\nAnswer 2')
file_path = 'FilesForFileHandling/words.txt'
with open(file_path, 'r') as file:
    file_content = file.read()
    words = file_content.split(' ')
print(len(words))

# Answer 3
print('\nAnswer 3')
file_path = 'FilesForFileHandling/output.txt'
content = 'Hello, Python!'
with open(file_path, 'w') as file:
    file.write(content)

# Answer 4
print('\nAnswer 4')
data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]
with open('FilesForFileHandling/students.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerows(data)
#
# 5. From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.

# Answer 5
print('\nAnswer 5')


def file_read_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.split('\n')


file_path = 'FilesForFileHandling/largeFile.txt'
data = file_read_generator(file_path)

for line in data:
    print(line)
