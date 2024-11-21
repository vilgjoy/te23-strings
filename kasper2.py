player = 1
turn = 1
max_turns = 10
print("Press Ctrl+C to stop loop")

while True:
    if turn % 7 == 0 or turn % 11 == 0 or '7' in str(turn) or '11' in str(turn):
        result = "clap"
    else:
        result = str(turn)

    print(f"Turn {turn}: Player -> {result}")
    if turn >= max_turns:
        print("Game set.")
        break
    player = 2 if player == 1 else 1

    turn += 1