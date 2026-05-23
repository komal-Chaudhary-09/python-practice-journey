# list

list = ["hello" , "my" , "name" , "is", "komal"] 
print(list)

list.append("choudhary")  #insert at end 
print(list)

sample = [1 ,2 , 34, 32, 22]
print(sample)
sample.sort()
print(sample)

sample.reverse()
print(sample)

sample.insert(4, 345)   #insert at partcular index
print(sample )

l = [4,5,6,8]
l.pop(1)
print(l)


#tupple

a = 1,2,4,3,3,3
print(a)

t = (10,20,3,45,43)
print(t[0])
print(t[-1])

 # tupple is immutable 
 
t1 = (1,2)
t2 = (3,4)
print(t1+t2)             #concatination

print(t1*3)              #repetition

print(20 in t)            #membership
print ("hello" in t )

print(len(t))

student = ("komal", 20 , "cs")
print(student)

fruits = []
f1 = input("enter fruits in the list ")
fruits.append(f1)
print(fruits)

students = []
marks = input("enter studnets marks")
students.append(marks)
print(students.sort())


a = (23, "komal", 98)
a[1] = " anu"
print (a[1])       # tuples cant be changed   


#to count zeroes in the given tupple 
p = (0,3,4,5,0,9,0,0)
n = p.count(0)
print(n)