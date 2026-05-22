#strings are not mutable 

name = "komal choudhary "
print(len(name))
print(name.endswith("mal"))
print(name.startswith("hek"))
print(name.capitalize())

index = name.find("k")
print(index)

replace = name.replace("komal", "anu")
print(replace)

text = "pYtHoN"
print(text.swapcase())

sample = "   hello world       "   #remove spaces 
print(sample.strip())

text = "car bike cake "       # convert string to list 
print(text.split())

text = " notebook23"
print(text.isalpha())      # only alphabets?



text = "bottle "
print(text.center(15))   # center align 

text = "charger"
print(text.encode())

text = "Python"

print(text.isascii())

text = "chair"

print("Py" in text)
print("Java" not in text)    #membership operators 

text = "table "

print(text[::-1])     # reverse string 