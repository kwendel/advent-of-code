import math
from pathlib import Path


def find_winning(time_range, total_time, record) -> int:
    winning = 0
    for time in time_range:
        distance = (total_time - time) * time
        if distance > record:
            winning += 1

    return winning


def find_losing(time_range, total_time, record) -> int:
    losing = 0
    for time in time_range:
        distance = (total_time - time) * time
        if distance <= record:
            losing += 1
        else:
            break

    return losing


def main():
    lines = Path("data/day_06.txt").read_text().split("\n")
    times = [int(n) for n in lines[0].split(":")[1].split(" ") if n != ""]
    records = [int(n) for n in lines[1].split(":")[1].split(" ") if n != ""]

    # Part 1
    ways_to_win = [
        find_winning(range(0, time + 1), time, record)
        for time, record in zip(times, records)
    ]
    print(f"Part 1: {math.prod(ways_to_win)}")

    # Part 2
    time, record = int("".join(map(str, times))), int("".join(map(str, records)))

    # Find the ways we can lose starting from 0 and from the starting time, until we win
    losing_from_bottom = find_losing(range(0, time + 1), time, record)
    losing_from_top = find_losing(range(time, 0, -1), time, record)

    print(f"Part 2: {time - (losing_from_bottom +losing_from_top) + 1}")


if __name__ == "__main__":
    main()
