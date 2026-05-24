#loops in python 


for i in range (6):      #A for loop is used when we know how many times we want to repeat something OR when we want to go through items one by one.
    print(i)
    
    
for i in range (1,10, 2):
    print(i)
    
name = "komal"
for ch in name:
    print(ch)
    
fruits = ["apple", "pen","book","hill"]
for fruit in fruits:
    print(fruit)


for i in range(3):
    for j in range(2):
        print(i,j)
        
# while loop we use when we dont know the condition

i = 1
while i <=5:
    print(i)
    i +=1 
    
for i in range(5):
    pass


for i in range(5):
    print("hello")
else:
    print("Loop finished")


# give index and value together
fruits =["apple", 'bananna',"mango"]

for index, value in enumerate(fruits):
    print(index, value)
    
names = ["komal", "riya"]
marks = [90, 85]

for n, m in zip (names, marks):
    print(n,m)
    
matrix =[]

for i in range(3):
    row =[]
    
    for j in range(3):
        row.append(j)
        
    matrix.append(row)
print(matrix)

text = "komal"
reverse =""
for ch in text:
    reverse = ch+reverse
print(reverse)


# practice questions

for i in range(1,20):
    print(i)

for i in range (1,10,2):
    print(i)
n = 5
fact = 1

for i in range (1,n+1):
    fact = fact*i
    print(fact)
    
text = " hello i am komal"
reverse =""

for ch in text:
    reverse = ch + reverse
print (reverse)
    
for i in range (1,6):
    print("*"*i)

list  =[1,4,2,5,7,98]
large = list[0]

for i in list :
    if i > large:
        large = i
print(large)

l = ["haary" ,"sahil","sachin","komal"]
for name in l:
    if(name.startswith("s")):
        print(f"hello {name}")

n = 5
i= 1
while(i<11):
    print(n*i)
    i+=1

n = 3

for i in range (2,n) :
     if(n%i==0):
      print("not prime")
      break;
    
else:
        print("prime")
n= 5
i=1
sum = 0
while (i<=n):
    sum +=i
    i +=1
print(sum)

n = int(input("enter the number"))
for i in range (1,n+1):
    if(i==1 or i==n):
        print("*" * n, end ="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end ="")
    print("")
    