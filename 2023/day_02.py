from collections import defaultdict
import math
from pathlib import Path


def parse_games(path: Path):
    with open(path, "r") as f:
        lines = f.readlines()

    games = {}
    for record in lines:
        game_id, results = record.strip().split(":")

        # Parse game ID
        game_id = int(game_id.split(" ")[1])

        # Parse into a list per color
        cubes_per_color = defaultdict(list)
        for hand in results.split(";"):
            for n_cube in hand.split(","):
                amount, cube = n_cube.strip().split(" ")
                cubes_per_color[cube].append(int(amount))

        games[game_id] = cubes_per_color

    return games


def main():
    # Parse data
    data_location = Path("data/day_02.txt")
    games = parse_games(data_location)

    # Part 1
    maxes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    # Make set of games which had any amount of cubes above the max
    invalid_games = {
        game_id
        for game_id, cubes_per_color in games.items()
        for color, amount in cubes_per_color.items()
        if any(n > maxes[color] for n in amount)
    }
    sum_of_valid_ids = sum(games.keys()) - sum(invalid_games)

    print(f"{invalid_games=}")
    print(f"Part 1: {sum_of_valid_ids=}")

    # Part 2
    # Take the sum of the game powers. A game power are the maximums of each color multiplied.
    powers_of_games = [
        math.prod([max(amount) for amount in cubes_per_color.values()])
        for cubes_per_color in games.values()
    ]
    print(f"Part 2: {sum(powers_of_games)=}")


if __name__ == "__main__":
    main()
