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
