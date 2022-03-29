print("˚⋆✧ Welcome to Sneeky Snack ✧⋆˚\n")

print(
    "Your teacher is currently teaching a lesson, but you are hungry.\nHowever eating is NOT allowed in the classroom.\nYour mission is to eat a snack without getting caught.\n\n")

# Write your code below this line 👇
print(
    "THE RULES:\n✧ This game uses single letter character commands. (E.g. 'Y' or 'y' = Yes)\n✧ To proceed in the game, ONLY type the command options presented to you at the time.\n✧ These command options will be placed within square brackets like so: [cmd1 cmd2]\n")

play = input("Are you ready to play? [Y or N] ").lower()

# Begin the game by asking what snack the player wants to eat


if play == "y":
    snack = input(
        "\n*** CLASS IS IN SESSION! ***\n\nPick a snack:\n[A = Potato Chips  B =  Peanuts  C = Gummy Bears] ").lower()

    if snack == "a":
        print(
            "\nYou opened the bag of chips and started eating.\nTeacher heard your munching.\nYou got caught.\n\n*** GAME OVER ***")


    elif snack == "b":
        print(
            "\nYou eat some peanuts.\nOH NO! Your Teacher starts wheezing and collapses on the floor.\nTurns out Teacher is allergic to nuts.\n\nAtleast you didn't get caught\n  *** YOU WIN ***")


    elif snack == "c":
        print(
            "\nYou eat the gummy bears.\nYum, these are great. Teacher doesn't suspect a thing.\nYou proceed to eat the rest.\n\n*** YOU WIN ***")

    else:
        print("You're too chicken and didn't choose a snack.\nYou stay hungry during the entire lesson.")

else:
    print("OK. See you next time.")

