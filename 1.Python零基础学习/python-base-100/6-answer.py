def fib1(x):
    a, b = 1, 1
    for i in range(x-1):
        a, b = b, a+b
    return a


def fib2(x):
    if(x == 1 or x == 2):
        return 1
    else:
        return fib2(x-1)+fib2(x-2)


def main():
    x = 10
    if(x == 0):
        print(0)
    if(x == 1 or x == 2):
        print(1)
    else:
        print("fib1=", fib1(x))
        print("fib2=", fib2(x))


main()
