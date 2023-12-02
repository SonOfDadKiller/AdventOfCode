input = open('pairs.txt').read().strip()

total = 0
for index, line in enumerate(input.split('\n')):
    ranges = line.split(',')
    vals = ranges[0].split('-') + ranges[1].split('-')
    min = [int(vals[0]), int(vals[2])]
    max = [int(vals[1]), int(vals[3])]

    if ((min[0] >= min[1] and min[0] <= max[1]) or (max[0] >= min[1] and max[0] <= max[1])) or ((min[1] >= min[0] and min[1] <= max[0]) or (max[1] >= min[0] and max[1] <= max[0])):
        total += 1

print(total)
