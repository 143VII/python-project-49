from brain_games.engine import run
from brain_games.games import calc


def main():
    run(calc.generate_round, calc.get_game_rules)


if __name__ == "__main__":
    main()
