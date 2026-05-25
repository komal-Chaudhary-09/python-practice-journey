with open("student.txt" ,"w") as f:
    f.write("komal\n")
    f.write("python learning\n")
    f.write("age : 20\n")
    
print("initial data written succesfully")

with open("student.txt" ,"r") as f:
    data = f.read()
    print("]\n------full file data----")
    print(data)
    
    
with open("student.txt" ,"a") as f:
    f.write("city : jaipur\n")
    f.write("course : python\n")
print("\n new data appneded sucessfully")

with open("student.txt" ,"r")  as f:
    print("\n----reading line by line---")
    
    line1 = f.readline()
    line2 = f.readline()
    
print("first line: ", line1)
print("second line: ", line2)


with open("student.txt" ,"r") as f:
    lines = f.readlines()
    print("\n -----readlines output-----" )
    print(lines)
    
for line in lines:
    print(line.strip())
    
with open("student.txt" ,"r") as f:
    print("\n ------cursor position-------")
    print("cursor position before reading:", f.tell())
    data= f.read(5)
    print("data read: ", data)
    
    print("cursor position after reading:", f.tell())
    
    
with open("student.txt", "r") as f:
    print("\n------seek function-------")
    
    print(f.read(5))
    
    f.seek(0)
    print("cursor moved back to start")
    print(f.read(5))
    
with open("student.txt","r") as f:
    data = f.read()
    words = data.split()
    print("\n Total words:",len(words))
    
    
with open("student.txt", "r") as f:
    data = f.read()
    print("\n------- searching word------")
    if"python" in data:
        print("python found")
    else:
        print("python was not found")
        
extra_lines =[
    "\nskills: AI",
    "\nskills : web d",
    
]
with open("student.txt","a") as f:
    f.writelines(extra_lines)
print("\n multiple lines added sucesfully")

with open("student.txt", "r") as source:

    # read original file data

    data = source.read()

# write same data into another file

with open("copy_student.txt", "w") as target:

    target.write(data)

print("\nFile copied successfully")

print("\n----- EXCEPTION HANDLING -----")

try:

    # this file does not exist

    with open("unknown.txt", "r") as f:
        print(f.read())

except FileNotFoundError:

    print("Error : File does not exist")
      
with open("student.txt", "r") as f:

    print("\n----- FINAL FILE DATA -----")

    print(f.read()) 