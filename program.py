inventory = []
lantern_lit = False

print("Welcome to this short tale traveler.")
print("You find yourself in a misty, ancient forest. Trees tall and twisted, the air filled with the scent of moss and wood.")
print("In front of you, there is a path leading deeper into the forest.")
print("Would you [explore] the path, walk the [other] way, or do [nothing], perhaps check your [inventory] to see if you have anything? You can end the adventure at any time by typing [exit]")

while True:
    action = input("What do you want to do? ").lower().replace("'", "").strip()

    if "explore" in action:
        print("You walk along the narrow path")
        print("After a short walk, you come across some kind of stone altar covered in moss.")
        print("")
        print("On the altar, you see a rusty lantern that still seems usable and a box but by your instinct, you can tell that if you choose one of them, the other will dissapear, would you like to take the [lantern] or open the [box]?")
        choice = input("What do you do? ").lower().replace("'", "").strip()

        if "lantern" in choice:
            print("The lantern looks old but sturdy. You decide to take it with you, you never know what will happen. The moment you touch the lantern, the box fades like it was never there.")
            inventory.append("lantern")
        elif "box" in choice:
            print("As you touch the box, the torch fades away like it was never there. You open the box and find a sparkling amulet. It glows with a faint light. You decide to take it with you, could maybe be valuable.")
            inventory.append("amulet")
        else:
            print("Maybe you should reconsider?")
        print("")
        print("You continue onward and discover a damp dark cave leading down. However, it is so dark you cannot see anything inside.")
        print("If only you had some light source, you could see whats inside the cave.")
        # Göra en input function här
        if lantern_lit == True:
            print("You hold the lantern upward and see that the cave is leading down. Like a force pulling you towards it, you decide that you should walk down to the cave below.")
        else:
            print("You try your best to see into the cave, but all you are met with is pure darkness, making it impossible to enter.")

    elif "other" in action:
        if "torch" not in inventory:
            print("You turn around and find a torch lying on the ground near a tree stump. You pick it up, it is a little bit wet, but it would still work if you lit it up.")
            inventory.append("torch")
        else:
            print("Somehow, you already got a torch, you dont need another one.")
        print("You continue to walk down the other path, but since there is not a clear distinction between the road, you appear to be lost. You can however hear a faint sound of fizzing sounds, like a fire.")

    elif "inventory" in action:
        print("You check inside your pocket and find...")
        if inventory == []:
            print("some lint and dust.")
        else:
            print("a", inventory)
            print("Maybe you can use something?")
            item_to_use = input("")

            if "torch" in item_to_use and "torch" in inventory:
                print("You light the torch. The warm glow lights up your surroundings.")
            elif "lantern" in item_to_use and "lantern" in inventory:
                if lantern_lit == True:
                    print("You put back the lantern to your hip and it the light inside dies out.")
                    lantern_lit = False
                else:
                    print("You hold up the lantern and suddenly it lights up your surroundings.")
                    lantern_lit = True
            elif "amulet" in item_to_use and "amulet" in inventory:
                print("You hold up the sparkling amulet. It radiates warmth and comfort, but you cannot pinpoint why or how.")
            else:
                print("You dont appear to have that in your inventory.")

    elif "exit" in action:
        print("Closing...")
        break
    else:
        print("It seems you cannot do that.")


