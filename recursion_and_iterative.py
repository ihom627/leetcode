#recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

a = input("enter recursive factorial number ")
print(factorial(a))

#iterative factorial
def iterative_factorial(n):
    total = 1 
    for i in range(1, n + 1):
        total = total * i
    return total

a = input("enter iterative factorial number ")
print(iterative_factorial(a))



#recursive fibonacci
def fibonacci(n):
    if (n == 0 ):
        return 0 
    elif (n == 1 ):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

a = input("enter the fibonacci number you want ")
print(fibonacci(a))


#iterative fibonacci
def iterative_fibonacci(n):
    temp = 0
    two_before =  0 
    one_before =  1 
    for i in range(2, n + 1):
        temp = one_before
        one_before = two_before + one_before
        two_before = temp
    return one_before

print(iterative_fibonacci(a))

#global vars

def printing_vars():
    global a
    print(a)
    a = "this is set inside printing_vars()"
    print(a)

a = "this is set as a global var"
printing_vars()


def openfile(filename):
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                print word
            print("\n")


openfile("foo.txt")

