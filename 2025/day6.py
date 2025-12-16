from functools import reduce
from operator import add, mul
#
# input = """
# 123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +  """

with open("./day6_input.txt") as infile:
    input = infile.read()

input_arr = input.strip().split("\n")
seperator_candidates = []
longest_lines = len(input_arr[0])
# print(input_arr)
for line in input_arr[:-1]:
    longest_lines = max(len(line), longest_lines)
    spaces = set()
    for idx, char in enumerate(line):
        if char == " ":
            spaces.add(idx)
    seperator_candidates.append(spaces)

seperators = set.intersection(*seperator_candidates)
seperators = sorted(seperators | {-1, longest_lines})
matrix = []
for line in input_arr[:-1]:
    nums = []
    for i in range(len(seperators) - 1):
        lower, upper = seperators[i] + 1, seperators[i + 1]
        nums.append(line[lower:upper])
    matrix.append(nums)
# print(matrix)
rows = len(matrix)
cols = len(matrix[0])
transpose = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
# print(transpose)

ops = [op for op in input_arr[-1] if op.strip()]
nums = []
for row in transpose:
    new_nums = ["" for _ in range(len(row))]
    for num in row:
        for idx, symbol in enumerate(num):
            if symbol != " ":
                new_nums[idx] += symbol
    # nums.append(new_nums)
    nums.append([num for num in new_nums if num])
print(nums)

total = 0
for idx, op in enumerate(ops):
    func = add if op == "+" else mul
    start = 0 if op == "+" else 1
    line_total = reduce(func, map(int, nums[idx]), start)
    # print(line_total)
    total += line_total
print(total)

# part1
# calculations = [[[], []] for _ in range(len(input_arr[0].split()))]
# # calculations = []
# # print(len(calculations))
#
# for row, line in enumerate(input_arr):
#     # print(row, line)
#     for col, num_str in enumerate(line.split()):
#         try:
#             if num_str.isdigit():
#                 calculations[col][0].append(int(num_str))
#             else:
#                 calculations[col][1].append(num_str)
#         except Exception as err:
#             print(row, col)
#
# # pprint(calculations)
#
# total = 0
# for symbols in calculations:
#     operands, operators = symbols
#     op = operators.pop()
#     start = 0 if op == "+" else 1
#     op = add if op == "+" else mul
#     total += reduce(op, operands, start)
#     print(operands, total)
#
# print(total)
