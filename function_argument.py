# def add(a,b,d=1):
#     c = a+b + d
#     return c
# x = add(5,2,4)
# print(x)
# supur = lambda a,b: a+b
# print(supur(5,6))
# suqare = lambda x: x*x
# print(suqare(5))

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(7))