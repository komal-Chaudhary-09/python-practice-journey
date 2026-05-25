# function and recusion in python practice

def wish():
    print("good morning user")
    
wish()

def goodday(name,ending ="thankue"):
    print(f"Good day,{name}")
    print(ending)
goodday("komal") 


square = lambda x: x*x

print(square(5))

# recursion 

def show(n):
    if n == 6:
        return 
    print(n)
    
    show(n+1)
show(1)

# factorial using recursion
def fact(n):
    if n == 1 or n==0 :
        return 1
    return n*fact(n-1)

print(fact(5))


# to find greatest of three number 
def great(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else :
        return c
    
print(great(8,9,3))


# function to conert celsius to fahernite 

def conversion(x):
    return 5*(x-32)/9


print(round(conversion(45)))

# pattern 
def pattern(n):
    if n == 0:
        return 
    print("*"*n)
    pattern(n-1)
pattern(3)

# multiplication table of one function
def multi(n):
    for i in range (1,11):
        print(f"{n} x {i} = {n*i}")
multi(5)
  