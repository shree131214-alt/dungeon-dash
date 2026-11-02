import random


def play_round():
    """Play one round and return 1 for a win, 0 for a draw, or -1 for a loss."""
    choices = {"1": "sword", "2": "shield", "3": "spell"}
    beats = {"sword": "spell", "spell": "shield", "shield": "sword"}

    print("\nChoose your move:")
    print("1. Sword")
    print("2. Shield")
    print("3. Spell")

    while True:
        player_move = input("> ").strip()
        if player_move in choices:
            break
        print("Please enter 1, 2, or 3.")

    player_move = choices[player_move]
    enemy_move = random.choice(list(choices.values()))
    print(f"You chose {player_move}. The dungeon creature chose {enemy_move}.")

    if player_move == enemy_move:
        print("It's a draw!")
        return 0
    if beats[player_move] == enemy_move:
        print("You win the round!")
        return 1

    print("The creature wins the round.")
    return -1


def main():
    print("=== DUNGEON DASH ===")
    print("Win two rounds to escape the dungeon!")

    player_score = 0
    creature_score = 0

    while player_score < 2 and creature_score < 2:
        result = play_round()
        if result > 0:
            player_score += 1
        elif result < 0:
            creature_score += 1
        print(f"Score — You: {player_score} | Creature: {creature_score}")

    if player_score == 2:
        print("\nYou escaped the dungeon. Victory!")
    else:
        print("\nThe creature caught you. Better luck next time!")


if __name__ == "__main__":
    main()
