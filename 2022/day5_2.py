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
        count = int(words[1])
        stack1 = int(words[3]) - 1
        stack2 = int(words[5]) - 1
        crates = stacks[stack1][-count:]

        for x in range(count):
            stacks[stack1].pop()

        stacks[stack2] += crates

for stack in stacks:
    print(stack.pop(), end="")