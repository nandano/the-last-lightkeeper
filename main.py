print("The Last Lightkeeper\n")

choice1 = input("You are standing at the edge of a cursed forest, the map trembling in your hand. The air is thick, the sky blood-red.\n" \
"You can either:\n" \
"1. Enter the Forest and brave the unknown\n2. Circle Around It to look for a safer path\n")

if choice1 == '1':
    choice2 = input("You meet a talking fox who offers to guide you for a price.\n" \
    "1. Trust the Fox and give him your silver pendant.\n2. Decline the Offer and try to find your way alone.\n")

    if choice2 == '1':
        choice3 = input("The fox guides you to a glowing portal deep in the woods.\n" \
        "1. Enter the Portal and take a leap of faith\n2. Thank the Fox but Walk Away because something feels off\n")
    
    elif choice2 == '2':
        choice4 = input("You get lost. Night falls fast.\nYou see two paths:\n" \
        "1. Follow the sound of water\n2. Head toward the distant light\n")

elif choice1 == '2':
    choice2 = input("You find a crumbling village and an old woman who warns you: \"The light tests your heart.\"\n" \
    "She offers you two gifts:\n1. A Mirror that shows you your true self.\n2. A Blade sharp enough to cut through illusions.\n")

    if choice2 == '1':
        choice3 = input("You see your reflection twisting into a monster - the darkness within you.\nYou must:\n" \
        "1. Face your fears and confront your darker self.\n2. Shatter the Mirror and deny what your just saw\n")

        if choice3 == '2':
            print("A true lighkeeper never denies their self.\nGame over!")
    
    elif choice2 == '2':
        choice3 = input("The blade hums in your hand. Shadows attack at nightfall.\nYou can either:\n" \
        "1. Fight the Shadows and stand your ground.\n2. Run toward the mountains and search for the sanctuary\n")
