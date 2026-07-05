'''def decorator(func):
    def wapper():
        print("Before function call")
        func()
        print("After function call")
    return wapper
@decorator
def say_hello():
    print("Hello world")
say_hello()'''

def decorator(func):
    def wapper(*args, **kwargs):
        print(f"Before adding call {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After adding call {func.__name__}")
        return result
    return wapper
@decorator
def number(a,b):
    print("The sum is:",a+b)
number(5,6)