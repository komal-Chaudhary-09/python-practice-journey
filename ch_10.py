with open("hello.txt","w") as f:
    f.write("\ntwinkle")
    f.write("\nlittle star")
    
with open("hello.txt","r") as f:
    data = f.read()
    if ("hqbwdhb") in data:
        print("found")
    else:
        print("not found")
        
        
def game():
    return 1
score = game()
print("current score :", score)
with open("hi-score.txt","r") as f:
    data = f.read()
    
if data == "":
    highscore = 0
else:
    highscore = int(data)
print("previous high score:",highscore)

if score>highscore:
    print("new high score acheived")
    
    with open("hi-score.txt","w") as f:
      f.write(str(score))
else:
    print("high score not broken")
    
    
    

import os

folder_names = "tables"

if not os.path.exists(folder_names):
    os.mkdir(folder_names)

print("folder ready:", folder_names)

for num in range(2,21):
    file_path =f"{folder_names}/{num}_table.txt"
    
    with open(file_path, "w") as f:
        for i in range(1,11):
            line = f"{num}X {i} = {num * i}\n"
            
            f.write(line)
    print(f"table of{num} created -> {file_path}")
    
print("\n all tables created successfully")

with open("student.txt","r") as f:
    data = f.read()
update_data = data.replace("donkey","######")

with open("students.txt","w") as f:
    f.write(update_data)
    
    
# ==================================================
# PROGRAM TO CENSOR MULTIPLE WORDS
# ==================================================


# LIST OF BAD WORDS

# 
# ============================================
# FIND LINE NUMBER WHERE "python" IS PRESENT
# ============================================


with open("log.txt", "r") as f:

    # read all lines into list

    lines = f.readlines()


# line number starts from 1

line_number = 1


# check each line

for line in lines:

    # convert line into lowercase
    # so Python, PYTHON, python all work

    if "python" in line.lower():

        print("Python found at line", line_number)

    # move to next line number

    line_number += 1

