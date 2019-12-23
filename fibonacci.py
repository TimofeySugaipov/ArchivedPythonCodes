import time #to measure the difference in time taken

#returns the nth fibonacci number using recursion

def fib(n):
    if n == 0:
        return 0
    elif n < 3:
        return 1
    return fib(n-1)+fib(n-2)

#returns the nth fibonacci number using a while loop

def lfib(n):
    a, b = 0, 1
    while (0<n):
        a, b = b, a+b
        n -=1
    return a

def timetaken(fun, n):
    start = time.time()
    fun(n)
    end = time.time()
    return str(fun) + " time taken: " + str(end - start)

#print(timetaken(fib, 40))
#<function fib at 0x03A14100> time taken: 30.57233738899231

#print(timetaken(lfib, 40))
#<function lfib at 0x039A4100> time taken: 0.0

#lfib is the faster function at high n values
