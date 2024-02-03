def fibonacci(i):
    for n in range(i):
        if n > 1:
            f = fib[-1] + fib[-2]
            fib.append(f)
        else:
            fib.append(n)
    else:
        return fib

if __name__ == "__main__":
    fib = []
    s = fibonacci(10)
    print(s)

'''
def fibonacci(n):
    a = 0
    b = 1
    while n >= 0:
        n -= 1
        yield a
        a, b = b, a+b

count = 0
for f in fibonacci(10):
    print(f)
'''


