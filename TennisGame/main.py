from TennisGame import TennisGame

def main():
    print("Welcome to the Tennis Game!")
    player_one = input("Enter the name of Player 1: ")
    player_two = input("Enter the name of Player 2: ")

    game = TennisGame(player_one, player_two)

    while True:
        print("\nCurrent Score:", game.get_score())
        scorer = input(f"Who scored? ({player_one}/{player_two}, or 'exit' to end): ").strip()

        if scorer.lower() == "exit":
            print("Game ended.")
            break
        elif scorer == player_one:
            game.player_one_scores()
        elif scorer == player_two:
            game.player_two_scores()
        else:
            print("Invalid input. Try again.")

        if game.has_winner():
            print(f"\n{game.get_score()}")
            print("Game over!")
            break

if __name__ == "__main__":
    main()
