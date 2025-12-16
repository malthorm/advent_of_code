from pprint import pprint

input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
# # part 1
# total = 0
# ranges = set()
# with open("./day5_input.txt") as infile:
#     for line in infile:
#         split_line = line.strip().split("-")
#         if len(split_line) == 2:
#             lower, upper = map(int, split_line)
#             ranges.add((lower, upper + 1))
#         elif line.strip():
#             num = int(line.strip())
#             for lower, upper in ranges:
#                 if lower <= num <= upper:
#                     total += 1
#                     break
#
# print(total)

# part 2
total = 0
ranges = []
with open("./day5_input.txt") as infile:
    for line in infile:
        if line == "\n":
            break
        split_line = line.strip().split("-")
        lower_curr, upper_curr = map(int, split_line)
        ranges.append((lower_curr, upper_curr))

ranges.sort(key=lambda x: x[0])

merged = [ranges[0]]
for i in range(1, len(ranges)):
    lower_curr, upper_curr = ranges[i]
    lower_last, upper_last = merged[-1]
    if lower_curr <= upper_last:
        last_merged = merged.pop()
        merged_range = (last_merged[0], max(upper_curr, upper_last))
        merged.append(merged_range)
    else:
        merged.append((lower_curr, upper_curr))


pprint(merged)
print(len(merged))

print(sum(end - start + 1 for (start, end) in merged))
