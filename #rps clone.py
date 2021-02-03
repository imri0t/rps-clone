#rps clone

from random import randint

print("Foot Nuke Cockroach\n(Quit ends)\n\n--im.ri0t")

game = True

comp = ["Nuke", "Foot", "Cockroach"]

gamesCounter = 0
winCounter = 0
tieCounter = 0

def over():
    print("You played {0} round(s), and won {1} round(s), playing tie in {2} round(s).".format(gamesCounter, winCounter, tieCounter))
    print("Hit enter to close")
    input()

while game == True:
    
    user = input(">>>").lower()


    if user == 'foot':
        print("You chose: Foot")
        compPick = comp[randint(0, 2)]

        if compPick == "Nuke":
            print("Computer chose: {}\nYou LOSE!".format(compPick))
            gamesCounter += 1

        elif compPick == "Foot":
            print("Computer chose: {}\nIt is a tie!".format(compPick))
            gamesCounter += 1
            tieCounter += 1
        
        elif compPick == "Cockroach":
            print("Computer chose: {}\nYou WIN!".format(compPick))
            gamesCounter += 1
            winCounter += 1


    elif user == 'nuke':
        print("You chose: Nuke")
        compPick = comp[randint(0, 2)]

        if compPick == "Nuke":
            print("Computer chose: {}\nBoth LOSE!".format(compPick))
            gamesCounter += 1

        elif compPick == "Foot":
            print("Computer chose: {}\nYou WIN!".format(compPick))
            gamesCounter += 1
            winCounter += 1
        
        elif compPick == "Cockroach":
            print("Computer chose: {}\nYou LOSE!".format(compPick))
            gamesCounter += 1


    elif user == 'cockroach':
        print("You chose: Cockroach")
        compPick = comp[randint(0, 2)]
        
        if compPick == "Nuke":
            print("Computer chose: {}\nYou WIN!".format(compPick))
            gamesCounter += 1
            winCounter += 1

        elif compPick == "Foot":
            print("Computer chose: {}\nYou Lose!".format(compPick))
            gamesCounter += 1
        
        elif compPick == "Cockroach":
            print("Computer chose: {}\nIt is a tie!".format(compPick))
            gamesCounter += 1
            tieCounter += 1


    elif user == 'quit':
        game = False
        over()


    elif user != "nuke" or "foot" or "cockroach":
        print("Incorrect selection.")