# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#c8ffc8")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy
    e "Hello, and welcome to my game!"
    e "Do you want to go outside or stay here with me?"
    menu:

        "Go outside.":
            jump outside
        "Stay in this room.":
            jump stay

    # This ends the game.
    label outside: 

        scene bg whitehouse with dissolve 
        show eileen concerned

        e "It's freezing out here!"
        return
    label stay: 

        show eileen happy
        e "Much better. It's warm in here."
        return
