input = open('crates.txt').read()

stacks = []

for i in range(0, 9):
    stacks.append([])

for index, line in enumerate(input.split('\n')):

    if index < 8:
        # parse stacks
        for i in range(0, 36, 4):
            c = line[i + 1]
            if c != ' ':
                stacks[int(i / 4)].insert(0, line[i + 1])
    elif index > 9:
        # parse commands
        words = line.split(' ')
        for x in range(int(words[1])):
            crate = stacks[int(words[3]) - 1].pop()
            stacks[int(words[5]) - 1].append(crate)
            # print(crate, end="\n")
        # print(stacks, end="\n\n")

for stack in stacks:
    print(stack.pop(), end="")