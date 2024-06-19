from brain_games.engine import run
from brain_games.games import even


def main():
    run(even.generate_round, even.get_game_rules)


if __name__ == "__main__":
    main()
