from functools import reduce
from operator import add, mul
from pprint import pprint

input = """
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """

# with open("./day6_input.txt") as infile:
#     input = infile.read()

input_arr = input.strip().split("\n")
seperator_candidates = []
for line in input_arr[:-1]:
    spaces = set()
    for idx, char in enumerate(line):
        if char == " ":
            spaces.add(idx)
    seperator_candidates.append(spaces)

seperators = set.intersection(*seperator_candidates)
seperators = sorted(seperators | {-1, len(input_arr[0])})
matrix = []
for line in input_arr[:-1]:
    nums = []
    for i in range(len(seperators) - 1):
        lower, upper = seperators[i] + 1, seperators[i + 1]
        nums.append(line[lower:upper])
    matrix.append(nums)

transpose = [
    [matrix[r][c] for r in range(len(input_arr[:-1]))] for c in range(len(input_arr[0]))
]

print(transpose)
# rows = len(input_arr)
# cols = len([num for num in input_arr[0].split(" ") if num.isdigit()])
# # print(rows, cols)
# matrix = []
# for line in input_arr:
#     row = []
#     for element in line.split(" "):
#         if element:
#             row.append(element)
#     matrix.append(row)
# transpose = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
#
# # pprint(matrix)
# # pprint(transpose)
#
# total = 0
# max_len = 0
# for row in transpose:
#     max_len = len(max(row, key=len))
#     op = row[-1]
#     for idx, num in enumerate(row[:-1]):
#         if len(num) < max_len:
#             if op == "+":
#                 row[idx] = num + "0" * (max_len - len(num))
#             elif op == "*":
#                 row[idx] = "0" * (max_len - len(num)) + num
#
#
# # pprint(transpose)
#
# total = 0
# for row in transpose:
#     nums = ["" for _ in range(max_len)]
#     op = row[-1]
#     for idx, num in enumerate(row[:-1]):
#         # digits = num.split("")
#         for idx, digit in enumerate(num):
#             nums[idx] += digit
#     start = 0 if op == "+" else 1
#     op = add if op == "+" else mul
#     line_total = reduce(op, map(int, nums), start)
#     total += line_total
#     print(nums, op, line_total)
# print(total)
# # print(nums)
#
#
# # part1
# # calculations = [[[], []] for _ in range(len(input_arr[0].split()))]
# # # calculations = []
# # # print(len(calculations))
# #
# # for row, line in enumerate(input_arr):
# #     # print(row, line)
# #     for col, num_str in enumerate(line.split()):
# #         try:
# #             if num_str.isdigit():
# #                 calculations[col][0].append(int(num_str))
# #             else:
# #                 calculations[col][1].append(num_str)
# #         except Exception as err:
# #             print(row, col)
# #
# # # pprint(calculations)
# #
# # total = 0
# # for symbols in calculations:
# #     operands, operators = symbols
# #     op = operators.pop()
# #     start = 0 if op == "+" else 1
# #     op = add if op == "+" else mul
# #     total += reduce(op, operands, start)
# #     print(operands, total)
# #
# # print(total)
