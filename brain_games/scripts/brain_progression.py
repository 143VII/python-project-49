from brain_games.engine import run
from brain_games.games import progression


def main():
    run(progression.generate_round, progression.get_game_rules)


if __name__ == "__main__":
    main()
