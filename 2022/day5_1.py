input = open('crates.txt').read()

stacks = []

for i in range(0, 8):
    stacks.append([])

for index, line in enumerate(input.split('\n')):

    if index < 8:
        # parse stacks
        for i in range(0, 36, 4):
            stacks[i].append(line[i + 1])
    # elif index > 11:
        # parse commands

print(stacks)