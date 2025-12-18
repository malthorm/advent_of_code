input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


with open("./day7_input.txt") as infile:
    input = infile.read()

splitters = set()

timelines = 0
input_arr = input.split("\n")
beams = set()
memo = {}
start = None
total = 0
for i, char in enumerate(input_arr[0]):
    if char == "S":
        beams.add((0, i))
        start = (0, i)
for i, line in enumerate(input_arr):
    for j, char in enumerate(list(line)):
        if char == "^":
            splitters.add((i, j))


left_right = []


def count_timelines(beam):
    x, y = beam
    if (x + 1, y) in memo:
        return memo[(x + 1, y)]
    if x == len(input_arr) - 1:
        return 1
    if (x + 1, y) in splitters:
        left = count_timelines((x + 1, y - 1))
        right = count_timelines((x + 1, y + 1))
        memo[(x + 1, y)] = left + right
        return left + right
    else:
        return count_timelines((x + 1, y))


print(count_timelines(start))

# # part1
# splitters = []
#
# total_splits = 0
# input_arr = input.split("\n")
# beams = set()
# for i, char in enumerate(input_arr[0]):
#     if char == "S":
#         beams.add((0, i))
#
# for i, line in enumerate(input_arr[:-1]):
#     # beams_on_line = beams[i]
#     for j, char in enumerate(line):
#         if char == "^" and (i - 1, j) in beams and (j - 1 > 0 or j + 1 < len(line)):
#             beams.add((i + 1, j - 1))
#             beams.add((i + 1, j + 1))
#             beams.remove((i - 1, j))
#             total_splits += 1
#         elif char == "." and (i - 1, j) in beams:
#             beams.add((i, j))
# print(beams)
# print(total_splits)
