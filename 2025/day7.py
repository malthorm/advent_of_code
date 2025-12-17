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


# with open("./day7_input.txt") as infile:
#     input = infile.read()

splitters = []

timelines = 0
input_arr = input.split("\n")
beams = set()
memo = {}
for i, char in enumerate(input_arr[0]):
    if char == "S":
        beams.add((0, i))

for i, line in enumerate(input_arr[:-1]):
    # beams_on_line = beams[i]
    for j, char in enumerate(line):
        if char == "^" and (i - 1, j) in beams and (j - 1 > 0 or j + 1 < len(line)):
            beams.add((i + 1, j - 1))
            beams.add((i + 1, j + 1))
            beams.remove((i - 1, j))
            # total_splits += 1
        elif char == "." and (i - 1, j) in beams:
            beams.add((i, j))


def count_timelines(start, beams):
    if start in memo:
        return memo[start]
    line_idx = start[0]
    if line_idx == len(input_arr) - 1:
        return 1
    for j, char in enumerate(input_arr[line_idx]):
        pass


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
