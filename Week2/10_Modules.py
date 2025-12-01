import datetime
import os

# Answer 1
print('\nAnswer 1')

current_date = datetime.datetime(2020, 3, 22)
print("Today : ", current_date)
print("After a week : ", current_date + datetime.timedelta(weeks=1))
print("After 12 hours : ", current_date + datetime.timedelta(hours=12))

# Answer 2
print('\nAnswer 2')

yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)
print("Yesterday: ", yesterday)
print("Today: ", today)
print("Tomorrow: ", tomorrow)

# Answer 3
print('\nAnswer 3')

current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")

test_directory = os.path.join(current_directory, 'test')
os.makedirs(test_directory, exist_ok=True)

print(f"Directory 'test' created at: {test_directory}")

print("Files and Folders in Current Directory:")
for item in os.listdir(current_directory):
    print(item)

if os.path.exists(test_directory):
    os.rmdir(test_directory)
    print("Directory 'test' removed.")
else:
    print("Directory 'test' does not exist.")

# Answer 4
print('\nAnswer 4')

old_filename = 'FilesForModules/old_file.txt'
new_filename = 'FilesForModules/new_file.txt'

if os.path.exists(old_filename):
    os.rename(old_filename, new_filename)
    print(f"Renamed {old_filename} to {new_filename}")
elif os.path.exists(new_filename):
    os.rename(new_filename, old_filename)
    print(f"Renamed {new_filename} to {old_filename}")


# Answer 5
print('\nAnswer 5')

file_path = 'FilesForModules/demo.txt'
content = 'I am a software engineer.'
with open(file_path, 'w') as file:
    file.write(content)

print(f'Size of the file is {os.path.getsize(file_path)} bytes')

# Answer 6
print('\nAnswer 6')

date_string = "Feb 25 2020 4:20PM"
date_object = datetime.datetime.strptime(date_string, "%b %d %Y %I:%M%p")
print(date_object.strftime("%Y-%m-%d %H:%M:%S"))

# Answer 7
print('\nAnswer 7')
date = datetime.datetime(2025, 2, 25, 16, 20)
past_date = date - datetime.timedelta(days=7)
print('New Date: ', past_date)

# Answer 8
print('\nAnswer 8')

date = datetime.datetime(2025, 2, 25)
past_date = date - datetime.timedelta(days=7)
print('New Date: ', past_date)

# Answer 9
print('\nAnswer 9')

date = datetime.datetime(2025, 2, 25)
print(date.strftime("%A" + " %d" + " %B" + " %Y"))
