def add(a,b,c):
    return a+b+c

print(add(3,4,5))

def myfunc(a,b):
    return a+b , a-b

print(myfunc(1,3))

double = lambda x : x * 2
print (double(5))

from math import sqrt
print(sqrt(25))
import datetime as d
print(d.datetime.now().time())

def factorial(n):
    if(n==1 or n==0):
        return 1

    return n * factorial(n-1)

n=int(input("enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")

a = 2
b = 3
c = 4

def greatest(a,b,c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>a and c>b):
          return c
   
   
print (greatest(a,b,c))