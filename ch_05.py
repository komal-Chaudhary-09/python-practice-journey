# sets practice

s ={1,2,3,4}
print(s)

a ={1 ,1,1,1,1,1,1}
print(a)

# s ={} worng this will create dictionary

p = set()
print(type(p))

o = { 3,5,6}
o.add(90)         # add single element
print(o)

n = {3,7,5}
n.update([34,4,4,4,42])     # add multiple elemnts 

print(n) 

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)

fs = frozenset([1,2,3])
print(fs)

math_students = {"Komal", "Riya", "Aman"}

science_students = {"Riya", "Aman", "Karan"}

print(math_students & science_students)


sets = { "18", 18}
print(sets)

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

dict ={}
name = input("enter frinds name ")
lang = input("enyter language")
dict.update({name: lang})
print(dict)