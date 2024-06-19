from brain_games.engine import run
from brain_games.games import prime


def main():
    run(prime.generate_round, prime.get_game_rules)


if __name__ == "__main__":
    main()
