from pathlib import Path


class AlmanacMapping:
    def __init__(self, list_of_ranges):
        self.ranges = list_of_ranges

    def __getitem__(self, key: int) -> int:
        for src, dst, length in self.ranges:
            # the key is not within this range
            if key not in range(src, src + length):
                continue

            # key is at the same offset from dst
            offset = key - src
            return dst + offset

        # Default: return the input again
        return key

    @classmethod
    def from_lines(cls, lines: list[str], reverse=False):
        list_of_ranges = []
        print(lines)
        for row in lines:
            print(row)
            dst, src, length = [int(n) for n in row.split(" ")]

            if reverse:
                list_of_ranges.append((dst, src, length))
            else:
                list_of_ranges.append((src, dst, length))

        return cls(list_of_ranges)


def main():
    # data_location = Path("./data/day_05.txt")
    data_location = Path("./data/day_05_example.txt")

    with open(data_location, "r") as f:
        lines = [stripped for line in f.readlines() if (stripped := line.strip()) != ""]

    seeds = [int(n) for n in lines[0].split(":")[1].strip().split(" ")]

    mappings_idx = [
        lines.index("seed-to-soil map:"),
        lines.index("soil-to-fertilizer map:"),
        lines.index("fertilizer-to-water map:"),
        lines.index("water-to-light map:"),
        lines.index("light-to-temperature map:"),
        lines.index("temperature-to-humidity map:"),
        lines.index("humidity-to-location map:"),
        len(lines),
    ]

    # # Part 1
    # mappings = []
    # for start, stop in zip(mappings_idx[::1], mappings_idx[1::1]):
    #     mappings.append(AlmanacMapping.from_lines(lines[start + 1 : stop]))

    # locations = []
    # for seed in seeds:
    #     outcome = seed
    #     for mapping in mappings:
    #         outcome = mapping[outcome]

    #     locations.append(outcome)

    # print(f"Part 1: {min(locations)}")

    extra_seeds = []
    for start, length in zip(seeds[::2], seeds[1::2]):
        extra_seeds.append(range(start, start + length))

    print(extra_seeds)

    mappings = []
    print(lines[-1])
    for start, stop in zip(mappings_idx[::1], mappings_idx[1::1]):
        print(start, stop)
        print(lines[start + 1 : stop])
        mappings.append(
            AlmanacMapping.from_lines(lines[start + 1 : stop], reverse=True)
        )

    mappings.reverse()
    location_map = mappings[0]

    lowest_dest = sorted([rang for rang in location_map.ranges], key=lambda r: r[0])
    print(lowest_dest)

    def evaluate(location):
        outcome = location
        for mapping in mappings:
            outcome = mapping[outcome]

        return outcome

    for num in range(0, 100):
        print(f"location={num} \t seed={evaluate(num)}")

    # for lower, _, length in lowest_dest:
    #     seed_lower = evaluate(lower)
    #     seed_upper = evaluate(lower + length)

    #     for seed, location in [(seed_lower, lower), (seed_lower, lower + length)]:
    #         for seed_range in extra_seeds:
    #             if seed in seed_range:
    #                 print(
    #                     f"In range: {seed=} \t from location={location} \t {seed_range=}"
    #                 )
    #                 break
    #         else:
    #             print(
    #                 f"Not in range: {seed=} \t from location={location}\t {seed_range=}"
    #             )
    #     # print(f"Location \t {lower} \t maps to \t {evaluate(lower)}")
    # print(f"Location \t {lower+length} \t maps to \t {evaluate(lower+length)}")
    # print()

    # for location in range(0, 50):
    #     print(f"Location \t {location} \t maps to \t {evaluate(location)}")
    #     print(f"Location \t {location} \t maps to \t {evaluate(location)}")
    #     print()

    # for loc in range(0, 397655230):
    #     seed_outcome = loc
    #     for mapping in mappings:
    #         seed_outcome = mapping[seed_outcome]

    #     # print(f"{seed_outcome}")
    #     for seed_range in extra_seeds:
    #         if seed_outcome in seed_range:
    #             print("I am fucking low")
    #             break
    # else:
    #     print("Not in a range")

    # locations = []
    # for i, seed in enumerate(seeds):
    #     outcome = seed
    #     for mapping in mappings:
    #         outcome = mapping[outcome]

    #     print(f"{i=} {seed=} {outcome=}")
    #     locations.append(outcome)

    # print(argmin(locations))


if __name__ == "__main__":
    main()
