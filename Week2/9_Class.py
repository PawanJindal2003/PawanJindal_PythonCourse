# Answer 1
print('\nAnswer 1')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello {self.name}, your age is {self.age}')


person1 = Person('Pawan', 21)
person1.greet()

# Answer 2
print('\nAnswer 2')


class BankAccount:
    total_balance = 0

    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name

    def deposit(self, amount):
        self.total_balance += amount
        print(f'Amount of {amount} deposited in your account.')

    def withdraw(self, amount):
        self.total_balance += amount
        print(f'Amount of {amount} withdrawn from your account.')

    def check_balance(self):
        print(f'Current Balance: {self.balance} deposited in your account.')


account1 = BankAccount(1, 1000, 'Pawan Jindal')
account1.deposit(1000)
account1.check_balance()
account1.withdraw(500)
account1.check_balance()

# Answer 3
print('\nAnswer 3')


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split(',', 1)
        return cls(title.strip(), author.strip())


book = Book.from_string("Python Programming, John Doe")
print(f"Title: {book.title}")
print(f"Author: {book.author}")

# Answer 4
print('\nAnswer 4')


class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def sound(self):
        return 'bark'


class Cat(Animal):
    def sound(self):
        return 'meow'


def make_sound(animal):
    print(f"The animal says: {animal.sound()}")


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)

# Answer 5
print('\nAnswer 5')


class DevOps:
    def __init__(self, model):
        self.model = model

    def deploy(self):
        return f"Can deploy the code using {self.model}."


class BackEnd:
    def __init__(self, language):
        self.language = language

    def write(self):
        return f"Can develop the application using {self.language}."


# Derived Class (Multiple Inheritance)
class SoftwareEngineer(DevOps, BackEnd):
    def __init__(self, name, company, language, model):
        BackEnd.__init__(self, language)
        DevOps.__init__(self, model)
        self.name = name
        self.company = company

    def about(self):
        return (f"{self.name} the Software Engineer from {self.company} is writing code in {self.language}"
                f" and deploying the application using {self.model}.")


sde = SoftwareEngineer("Pawan Jindal", "TTN", "Java", "Kubernetes")
print(sde.write())
print(sde.deploy())
print(sde.about())
