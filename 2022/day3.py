input = open('items.txt').read().strip()

total = 0
elfs = []
for index, line in enumerate(input.split('\n')):

    elfs.append(line)

    if (index + 1) % 3 == 0:
        common = list(set(elfs[0]).intersection(elfs[1]).intersection(elfs[2]))[0]
        for i, c in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']):
            if common.lower() == c:
                if common.isupper():
                    total += i + 1 + 26
                else:
                    total += i + 1
        elfs = []

print(total)
