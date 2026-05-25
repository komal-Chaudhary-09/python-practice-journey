# rock paper and scissor 
import random
computer = random.choice([-1,0,1])

youstr = input("enter your choice(r,p,s):")

youDict = {
    "r": 1,
    "p": -1,
    "s": 0
}

reverseDict ={
    1 : "rock",
    -1: "paper",
    0: "scissor"
}
you = youDict[youstr]
print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a Draw!")
    
else:

    # Computer chose Rock
    if computer == 1 and you == -1:
        print("You Win!")

    elif computer == 1 and you == 0:
        print("You Lose!")

    # Computer chose Paper
    elif computer == -1 and you == 1:
        print("You Lose!")

    elif computer == -1 and you == 0:
        print("You Win!")

    # Computer chose Scissors
    elif computer == 0 and you == 1:
        print("You Win!")

    elif computer == 0 and you == -1:
        print("You Lose!")   
