import random

# Board configuration: keys are positions of snakes or ladders
# Values for ladders are higher than keys (moving up), for snakes are lower (moving down)
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Initialize player positions
player_position = [0, 0]

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to move player
def move_player(player, roll):
    print(f"Player {player + 1} rolled a {roll}")
    player_position[player] += roll

    # Check for ladders
    if player_position[player] in ladders:
        print(f"Player {player + 1} climbed a ladder from {player_position[player]} to {ladders[player_position[player]]}")
        player_position[player] = ladders[player_position[player]]

    # Check for snakes
    elif player_position[player] in snakes:
        print(f"Player {player + 1} got bitten by a snake from {player_position[player]} to {snakes[player_position[player]]}")
        player_position[player] = snakes[player_position[player]]

    # Ensure player does not exceed 100
    if player_position[player] > 100:
        player_position[player] -= roll
        print(f"Player {player + 1} exceeded 100 and stays at {player_position[player]}")

    print(f"Player {player + 1} is now at position {player_position[player]}")

# Main game loop
def play_game():
    player = 0
    while True:
        input(f"\nPlayer {player + 1}'s turn. Press Enter to roll the dice...")
        roll = roll_dice()
        move_player(player, roll)

        # Check for winning condition
        if player_position[player] == 100:
            print(f"\nCongratulations! Player {player + 1} wins!")
            break

        # Switch players
        player = 1 - player

play_game()
