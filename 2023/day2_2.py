input = open('cubes.txt').read().strip()

total = 0
for index, line in enumerate(input.split('\n')):
    rounds = line.split(':')[1].split(';')
    redMin = 0
    greenMin = 0
    blueMin = 0
    for r in rounds:
        cubes = r.split(',')
        for c in cubes:
            val = int(c.strip().split(' ')[0])
            color = c.strip().split(' ')[1]

            if color == 'red':
                redMin = max(redMin, val)
            if color == 'green':
                greenMin = max(greenMin, val)
            if color == 'blue':
                blueMin = max(blueMin, val)

    total += redMin * greenMin * blueMin

print(total)

# 12 red cubes, 13 green cubes, and 14 blue cubes