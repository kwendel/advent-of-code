from pathlib import Path
import numpy as np


# def to_set(numbers) -> set[int]:
#     return set(int(w) for w in numbers.strip().split(" ") if w != "")


def main():
    # data = Path("./data/day_04_example.txt")
    data = Path("data/day_04.txt")

    # Parse cards input into list of tuples with 0=winning and 1=actual numbers
    cards = [
        line.strip().split(":")[1].split("|") for line in data.read_text().split("\n")
    ]
    # the winning numbers are in both sets = intersection of the sets
    to_set = lambda numbers: set(int(n) for n in numbers.strip().split(" ") if n != "")
    wins_per_card = [len(to_set(card[0]) & to_set(card[1])) for card in cards]

    # Part 1
    total_worth = [2 ** (wins - 1) for wins in wins_per_card if wins > 0]
    print(f"Part 1: {sum(total_worth)=}")

    # Part 2
    # Spread the wins over the next cards, multiplied by wins of that cards if we already won extra cards
    total_cards = np.ones(len(cards), dtype=int)
    for card_i, wins in enumerate(wins_per_card):
        total_cards[card_i + 1 : card_i + 1 + wins] += 1 * total_cards[card_i]
    print(f"Part 2: {sum(total_cards)=}")


if __name__ == "__main__":
    main()
