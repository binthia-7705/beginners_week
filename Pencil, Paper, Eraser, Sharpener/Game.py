import random

def choice(c):
    if c==1:
        choice="Pencil"
    elif c==2:
        choice="Paper"
    elif c==3:
        choice="Eraser"
    elif c==4:
        choice="Sharpener"
    else:
        choice="Invalid"
    return choice

#Rules for playing the game
print("RULES FOR PENCIL, PAPER, ERASER AND SHARPENER GAME ")
print("1. Pencil vs Paper >>>>> Pencil wins ")
print("2. Pencil vs Eraser >>>>> Eraser wins ")
print("3. Pencil vs Sharpener >>>>> Sharpener wins ")
print("4. Paper vs Eraser >>>>> Paper wins ")
print("5. Paper vs Sharpener >>>>> Sharpener wins ")
print("6. Eraser vs Sharpener >>>>> Eraser wins ")

#Dictionary with winning cases of the game
winning_cases = {
    (1, 2): "Pencil",      # Pencil beats Paper
    (3, 1): "Eraser",      # Eraser beats Pencil
    (4, 1): "Sharpener",   # Sharpener beats Pencil
    (2, 3): "Paper",       # Paper beats Eraser
    (4, 2): "Sharpener",   # Sharpener beats Paper
    (3, 4): "Eraser"       # Eraser beats Sharpener
}

while True:
    #Choices for player
    print("\nChoose your option: ")
    print("1. Pencil")
    print("2. Paper")
    print("3. Eraser")
    print("4. Sharpener")
    c=int(input("Enter your choice: "))

    #Error message
    if c<1 or c>4:
        print("Error: Invalid Choice\n")
        continue

    #Choice by player
    print("\nUser's choice: ",choice(c))

    #Choice by computer
    comp_c=random.randint(1,4)
    print("Computer's choice: ",choice(comp_c))

    #Determining the winner
    if c == comp_c:
        print("\n<<<<<<<<<< It's a tie >>>>>>>>>>")
    elif (c, comp_c) in winning_cases:
        print("\n<<<<<<<<<< User Wins >>>>>>>>>>")
    elif (comp_c, c) in winning_cases:
        print("\n<<<<<<<<<< Computer Wins >>>>>>>>>>")

    #Asking if the player wants to play again
    x=input("\nDo you want to play again (Y/N) ?: ")
    if x=="N":
        break

#Ending the game message
print("Thank You for Playing")
