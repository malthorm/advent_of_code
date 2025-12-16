# part1
# with open("./day3_input.txt") as infile:
#     total = 0
#     for line in infile:
#         line = line.strip()
#         current_max = int(line[0])
#         biggest_after_max = int(line[1])
#         for idx in range(1, len(line)):
#             num = int(line[idx])
#             if idx != len(line) - 1 and num > current_max:
#                 current_max = num
#                 biggest_after_max = int(line[idx + 1])
#             else:
#                 if num > biggest_after_max:
#                     biggest_after_max = num
#         total += current_max * 10 + biggest_after_max
#
# print(total)

total_joltage = 0
with open("./day3_input.txt") as infile:
    for line in infile:
        line = line.strip()
        bank_len = len(line)
        stack = []
        for i in range(bank_len):
            while stack and line[i] > stack[-1] and len(stack) + bank_len - i > 12:
                stack.pop()
            stack.append(line[i])
        while len(stack) > 12:
            stack.pop()
        total_joltage += int("".join(stack))

print(total_joltage)
