max_turns = 50

turn = 1
player = 1

for turn in range(1, max_turns + 1):
    if turn % 7 == 0 or turn % 11 == 0 or '7' in str(turn) or '11' in str(turn):
        result = "clap"
    else:
        result = str(turn)

    print(f"Turn {turn}: Player -> {result}")

    player = 2 if player == 1 else 1

