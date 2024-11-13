inventory = []

print("Welcome to this short tale traveler.")
print("You find yourself in a misty, ancient forest. Trees tall and twisted, the air filled with the scent of moss and wood.")
print("Infront of you, there is a path leading deeper into the forest.")
print("Would you [explore] the path, walk the [other] way, or do [nothing]?")

action = input("What do you want to do? ").lower().replace("'", "").strip()

if "explore" in action:
    print("You walk along the narrow path")
    print("After a short walk, you come across some kind of stone altar covered in moss.")
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

elif "other" in action:
    if "torch" not in inventory:
        print("You turn around and find a torch lying on the ground near a tree stump. You pick it up, it is a little bit wet, but it would still work if you lit it up.")
        inventory.append("torch")
    else:
        print("Somehow, you already got a torch, you dont need another one.")
    print("You continue to walk down the other path, but since there is not a clear distinction between the road, you appear to be lost. You can however hear a faint sound of fizzing sounds, like a fire.")


