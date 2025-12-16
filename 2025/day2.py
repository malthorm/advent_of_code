# input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659, 824824821-824824827,2121212118-2121212124"
id_ranges = []
max_num = 0
total = 0
with open("./day2_input.txt") as infile:
    input = infile.read()
    for id_range in input.split(","):
        lower, upper = map(int, id_range.split("-"))
        if upper > max_num:
            max_num = upper
        id_ranges.append((lower, upper))

invalid_ids = set()


for i in range(1, 10 ** (len(str(max_num)) // 2) + 1):
    for j in range(2, len(str(max_num))):
        x = int(str(i) * j)

        for lower, upper in id_ranges:
            if lower <= x <= upper:
                invalid_ids.add(x)

print(len(invalid_ids))
print(sum(invalid_ids))


# for id_range in id_ranges:
#     lower, upper = id_range.split("-")
#
#     for _id in range(int(lower), int(upper) + 1):
#         num_str = str(_id)
#         num_digits = len(num_str)
#
#         for digit_len in range(num_digits // 2, 0, -1):
#             # repeatable sequence requires even split
#             if num_digits % digit_len != 0:
#                 continue
#
#             sequence_set = set()
#             for pos in range(0, num_digits, digit_len):
#                 sequence_set.add(num_str[pos : pos + digit_len])
#
#             if len(sequence_set) == 1:
#                 total += int(num_str)
#                 break
#

# print(total)
