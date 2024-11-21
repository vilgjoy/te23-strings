player = 1
turn = 1
max_turns = 20
print("Press Ctrl+C to stop loop")

while True:
    if turn % 3 == 0  and turn % 5 == 0:
        result = "oompaloompa"
    elif turn % 3 == 0:
        result = "oompa"
    elif turn % 5 == 0:
        result = "loompa"
    else:
        result = str(turn)

    print(f"Turn {turn}: Player -> {result}")
    if turn >= max_turns:
        print("Game set.")
        break
    player = 2 if player == 1 else 1

    turn += 1