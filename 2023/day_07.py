from collections import defaultdict
from pathlib import Path


card_numbers = {
    "A": , 
    "K": , 
    "Q": , 
    "J": , 
    "T": , 
    "9": , 
    "8": , 
    "7": , 
    "6": , 
    "5": , 
    "4": , 
    "3": , 
    "2": 
    }


def main():
    data_location = Path("data/day_07_example.txt")
    lines = data_location.read_text().split("\n")
    hands = [n.split(" ")[0] for n in lines]
    bids = [int(n.split(" ")[1]) for n in lines]

    sorted_hands = defaultdict(list)
    for hand in hands:
        unique = len(set(hand))
        vals = sorted([hand.count(elem) for elem in set(hand)], reverse=True)
        match unique, vals:
            case 1, _:
                kind = "five_kind"
            case 2, [4, 1]:
                kind = "four_kind"
            case 2, [3, 2]:
                kind = "full_house"
            case 3, [3, 1, 1]:
                kind = "three_kind"
            case 3, [2, 2, 1]:
                kind = "two_pair"
            case 4, [2, 1, 1, 1]:
                kind = "one_pair"
            case 5, [1, 1, 1, 1, 1]:
                kind = "high_card"
            case _:
                print("Error: ", hand, unique, vals)

        sorted_hands[kind].append(hand)

    for cards in sorted_hands["five_kind"]:
        print(kind)

    print(sorted_hands)


if __name__ == "__main__":
    main()
