#Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!".
#Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.
'''def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function is being called {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
@decorator
def say_hello():
    print("Hello!")
say_hello()'''

def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper
@timer
def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
        n += 1
    return total

# Test the timer decorator
result = sum_numbers(1000000)
print(f"Sum: {result}")