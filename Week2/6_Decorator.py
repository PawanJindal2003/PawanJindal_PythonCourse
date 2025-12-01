from datetime import datetime

# Answer 1
print("\nAnswer 1")


def cal_time_appending_numbers(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print("Total time taken: ", end_time - start_time)
        return result

    return wrapper


@cal_time_appending_numbers
def append_numbers(nums, a=1):
    while a <= 1000:
        nums.append(a)
        a += 1


nums = []
append_numbers(nums)

# Answer 2
print("\nAnswer 2")


def retry(attempts):
    def decorator(func):

        def wrapper(*args, **kwargs):
            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
            print("All attempts exhausted")

        return wrapper

    return decorator


@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")


may_fail("Pawan Jindal")

# Answer 3
print("\nAnswer 3")


def validate_positive(func):
    def wrapper(x):
        if x < 0:
            print("Argument must be positive.")
            return None
        return func(x)

    return wrapper


@validate_positive
def square_root(x):
    return x ** 0.5


print(square_root(-10))

# Answer 4
print("\nAnswer 4")


def cache(func):
    cache_dict = {}

    def wrapper(x):
        key = x
        if key in cache_dict:
            print("Retrieving result from cache...")
            return cache_dict[key]
        result = func(x)
        cache_dict[key] = result
        return result

    return wrapper


@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x


print(expensive_computation(5))
print(expensive_computation(5))

# Answer 5
print("\nAnswer 5")


def is_admin(func):
    def wrapper(user, user_id):
        permissions_list = user['permissions']
        if 'admin' in permissions_list:
            return func(user, user_id)
        else:
            print('Access Denied')

    return wrapper


@is_admin
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")


user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}

delete_user(user1, 1)
delete_user(user2, 2)
