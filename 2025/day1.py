# sample_intput = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
#
# dial_pos = 50
# count_zeros = 0
#
# for rotation in sample_intput:
#     direction, value = rotation[0].lower(), int(rotation[1:])
#
#     while value > 100:
#         count_zeros += 1
#         value -= 100
#
#     if direction == "l":
#         if dial_pos - value < 0 and dial_pos != 0:
#             count_zeros += 1
#         dial_pos = (dial_pos - value) % 100
#     else:
#         if dial_pos + value > 100 and dial_pos != 0:
#             count_zeros += 1
#         dial_pos = (dial_pos + value) % 100
#
#     if dial_pos == 0:
#         count_zeros += 1


# dial_pos = 50
# count_zeros = 0
#
# with open("./day1_input.txt") as infile:
#     for rotation in infile:
#         rotation = rotation.strip()
#         direction, value = rotation[0].lower(), int(rotation[1:])
#
#         while value > 100:
#             count_zeros += 1
#             value -= 100
#
#         if direction == "l":
#             if dial_pos - value < 0 and dial_pos != 0:
#                 count_zeros += 1
#             dial_pos = (dial_pos - value) % 100
#         else:
#             if dial_pos + value > 100 and dial_pos != 0:
#                 count_zeros += 1
#             dial_pos = (dial_pos + value) % 100
#
#         if dial_pos == 0:
#             count_zeros += 1
#
# print(count_zeros)


start_pos = 50

current_pos = start_pos
count_zeros = 0

with open("./day1_input.txt") as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue

        direction = line[0].upper()
        value = int(line[1:])

        step = value if direction == "R" else -value

        if step > 0:
            # multiples of 100 in [current_pos, current_pos + step]
            count_zeros += (current_pos + step) // 100 - current_pos // 100
        elif step < 0:
            # multiples of 100 in [current_pos + step, current_pos]
            count_zeros += (current_pos - 1) // 100 - (current_pos + step - 1) // 100

        current_pos += step

    print(count_zeros)
