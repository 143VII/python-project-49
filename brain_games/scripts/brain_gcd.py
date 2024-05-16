from brain_games.engine import run
from brain_games.games import gcd

def main():
    run(gcd.generate_round, gcd.get_game_rules)

if __name__ == "__main__":
    main()
