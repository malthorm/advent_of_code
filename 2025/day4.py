# input = """
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""
#
with open("./day4_input.txt") as infile:
    input = infile.read()


def accessible(paper_pos: tuple[int, int]) -> bool:
    row, col = paper_pos
    total_free = 0
    to_check = [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    ]

    for pos in to_check:
        if pos in free_positions:
            total_free += 1
    return total_free > 4


free_positions = set()
paper_positions = []
lines = [line.strip() for line in input.split()]
removed_positions = set()

free_positions.update({(-1, col) for col in range(-1, len(lines[0]) + 1)})
free_positions.update({(len(lines), col) for col in range(-1, len(lines[0]) + 1)})
free_positions.update({(row, -1) for row in range(len(lines))})
free_positions.update({(row, len(lines[0])) for row in range(len(lines))})

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == ".":
            free_positions.add((i, j))
        else:
            paper_positions.append((i, j))

total = 0
removed_paper = True
i = 0
while paper_positions and removed_paper:
    new_queue = []
    new_free = set()
    for paper_pos in paper_positions:
        i += 1
        removed_paper = False
        if accessible(paper_pos):
            removed_paper = True
            new_free.add(paper_pos)
            removed_positions.add(paper_pos)
            total += 1
        if not removed_paper:
            new_queue.append(paper_pos)
    removed_paper = len(new_queue) != len(paper_positions)
    paper_positions = new_queue
    free_positions.update(new_free)
    print(total)  # 8112
    print(i)  # num of iterations necessary
