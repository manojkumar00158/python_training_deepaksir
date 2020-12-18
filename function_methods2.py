#default positional arguments
def addition (a,b):
    return a + b

if __name__ == '__main__':
    a = 2
    b = 4
    print(addition(a,b))

#key worded arguments
def multiplication (a,b ):
    return a * b

if __name__ == '__main__':
    a = 4
    
    print(multiplication(a,b = 2))

#*args arguments
def division(*args):
    a,b = args
    return a/b

if __name__ == '__main__':
    a = 10
    b = 5
    print(division(a,b))


def factorial(n):

    i = 0
    result = 1
    while(i != n):
        i = i + 1
        result = result * i
    return result

if __name__ == '__main__':
    n = 5
    print(factorial(n))

def substraction(a,b):
    return a - b

if __name__ == '__main__':
    print(substraction(a=8,b=4))


def even_odd(c):

    if (c % 2) == 0:
        print(c,"is even number" )
    else:
        print(c,"is odd number")
        


if __name__ == '__main__':
    c = 4
    even_odd(c)




    


