import random

l = ["rock", "scissor", "paper"]

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
                 Game start -----
                 1. Yes 
                 2. No| Exit
                 '''))

    if uc == 1:
        for a in range(1, 6):
            userInput = int(input('''
                             1. Rock 
                             2. Scissor
                             3. Paper
                             '''))

            if userInput == 1:
                unchoice = "rock"
            elif userInput == 2:
                unchoice = "scissor"
            elif userInput == 3:
                unchoice = "paper"

            cchoice = random.choice(l)

            if cchoice == unchoice:
                print("Computer value: ", cchoice)
                print("User value: ", unchoice)
                print("Game Draw")
                ucount += 1
                ccount += 1

            elif (unchoice == "rock" and cchoice == "scissor") or (unchoice == "paper" and cchoice == "rock") or (unchoice == "scissor" and cchoice == "paper"):
                print("Computer value:", cchoice)
                print("User value:", unchoice)
                print("You Win")
                ucount += 1

            else:
                print("Computer value:", cchoice)
                print("User value:", unchoice)
                print("Computer Win")
                ccount += 1

    elif uc == 2:
        break

if ucount == ccount:
    print("Final Game Draw.....")
    print("User Score: ", ucount)
    print("Computer Score: ", ccount)

elif ucount > ccount:
    print("Final You Win ....")
    print("User Score:", ucount)
    print("Computer Score:", ccount)

else:
    print("Computer Win...")
    print("User Score:", ucount)
    print("Computer Score:", ccount)
