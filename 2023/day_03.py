import math
from pathlib import Path
from more_itertools import consecutive_groups


class EngineSchema:
    def __init__(self, data_location: Path):
        # self.divider = "."

        with open(data_location, "r") as f:
            lines = f.readlines()

        self.idx_numbers = {}
        self.idx_symbols = {}
        for row, line in enumerate(lines):
            line = line.strip()

            numbers = []
            symbols = []
            for idx, char in enumerate(line):
                # skip dividers
                if char in [".", "", " "]:
                    continue

                if char.isdigit():
                    numbers.append(idx)
                else:
                    symbols.append(idx)

            for si in symbols:
                self.idx_symbols[(row, si)] = line[si]

            for idx in consecutive_groups(numbers):
                idx = list(idx)
                start = idx[0]
                end = idx[-1]
                value = int(line[start : end + 1])

                for col in range(start, end + 1):
                    self.idx_numbers[(row, col)] = value

        # print(self.idx_numbers)
        # print(self.idx_symbols)


def adjacent(row: int, column: int) -> list[tuple[int, int]]:
    cols = range(column, column + 1)
    possible_locations = []

    # Above
    possible_locations.extend([(row - 1, col) for col in cols])
    # Diagonal above
    possible_locations.extend([(row - 1, column - 1), (row - 1, column + 1)])
    # Under
    possible_locations.extend([(row + 1, col) for col in cols])
    # Diagonal under
    possible_locations.extend([(row + 1, column - 1), (row + 1, column + 1)])
    # Sides
    possible_locations.extend([(row, column - 1), (row, column + 1)])

    return possible_locations


def part_1(schema: EngineSchema):
    part_numbers = set()

    for (row, col), symbol in schema.idx_symbols.items():
        for loc in adjacent(row, col):
            connected_part = schema.idx_numbers.get(loc, None)

            if connected_part:
                part_numbers.add(connected_part)

                # print(f"{symbol=} connected to part={connected_part}")

    print(part_numbers)
    print(f"Part 1: {sum(part_numbers)=}")

    # for idx, number in schema.idx_numbers.items():
    #     row, (start, end) = idx

    #     for loc in adjacent(row, start, end):
    #         adjacent_symbol = schema.idx_symbols.get(loc, None)

    #         if adjacent_symbol:
    #             # print(number, adjacent_symbol)
    #             total += number

    # print(f"{total=}")


def part_2(schema: EngineSchema):
    gears = [loc for loc, symbol in schema.idx_symbols.items() if symbol == "*"]
    gear_ratios = []

    for row, col in gears:
        # Find the connected parts
        connected = set()
        for loc in adjacent(row, col):
            part = schema.idx_numbers.get(loc, None)
            if part:
                connected.add(part)

        # Add gear ratio (product) when only 2 parts connected
        if len(connected) == 2:
            gear_ratios.append(math.prod(connected))

    print(f"Part 2: {sum(gear_ratios)=}")


def part_2_oneline(schema: EngineSchema):
    gear_ratios = [
        math.prod(parts)
        for parts in [
            {
                schema.idx_numbers.get(loc, None)
                for loc in adjacent(row, col)
                # walrus operator is not allowed in if-statement?
                if schema.idx_numbers.get(loc, None)
            }
            for row, col in [
                loc for loc, symbol in schema.idx_symbols.items() if symbol == "*"
            ]
        ]
        if len(parts) == 2
    ]

    print(f"Part 2: {sum(gear_ratios)=}")


def main():
    # create 2d data structure of input
    # data_location = Path("./data/day_03_example.txt")
    data_location = Path("data/day_03.txt")
    schema = EngineSchema(data_location)

    # Part 1
    # part_1(schema)

    # Part 2
    part_2(schema)
    part_2_oneline(schema)


if __name__ == "__main__":
    main()
