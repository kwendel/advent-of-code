from pathlib import Path

data_file = "data/day_01.txt"
# data_file = "data/day_01_example.txt"
raw_data = Path(data_file).read_text().split("\n")

parts = [line.split() for line in raw_data if line]
left = [int(l) for l, _ in parts]
right = [int(r) for _, r in parts]

# Part 1: total distance between sorted left and right
diffs = [abs(l - r) for l, r in zip(sorted(left), sorted(right))]
total = sum(diffs)
print("Part 1:", total)

# Part 2: similarity score
occurrence_right = {r: right.count(r) for r in right}
scores = [l * occurrence_right[l] for l in left if l in occurrence_right]
score = sum(scores)
print("Part 2:", score)



