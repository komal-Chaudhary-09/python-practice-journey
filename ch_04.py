# dictionary and sets 
marks = {
    "komal": 100,
    "anu": 28,
    "uma": 34
    }
print(marks.items()) 
marks.update({"komal": 9800})
print(marks)

print(marks.get("komal")) # it will give none if key dosnt exist 
print(marks["komal"]) # it will give error of key does not exist 

marks.clear()
print(marks)

students = {
    "name": "komal",
    "age" : 60
}
students["friend"] = "anu"      # adding element 
print (students)

students.pop("age")     # removing element
print(students)


students.popitem()   # will remove last item 

del students["name"]
students.clear()       # removes everything


student = {
    "name": "Komal",
    "age": 20
}

for x in student.values():
    print(x)
    
for key, value in student.items():
    print(key,value)
    
keys = ("a", "b","c","d")
x = dict.fromkeys(keys, 0)
print(x)

# nested dictionary 

students = {
    "student1": {
        "name" : "komal",
        "age" : 20
    },
    "student2": {
        "name": "riya",
        "age" : 32
    }
}
print(students["student1"]["name"])


# reverse key and value
dict = {
     "a": 1,
     "b" :2
 }
new = {}
for key, value in dict.items():
    new[value] = key
print (new)


# count frequncy of characters 
text ='apple'
freq ={}
for ch in text:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch] =1
print(freq)

hello ={
    "first": 20,
    "second": 30,
    "third": 20
}
print(hello)
 