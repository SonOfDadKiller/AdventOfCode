input = open('cubes.txt').read().strip()

total = 0
for index, line in enumerate(input.split('\n')):
    games = line.split(':')[1].split(';')
    valid = True
    for g in games:
        
        rounds = g.split(',')
        for r in rounds:
            val = int(r.strip().split(' ')[0])
            color = r.strip().split(' ')[1]

            if color == 'red' and val > 12:
                valid = False
            if color == 'green' and val > 13:
                valid = False
            if color == 'blue' and val > 14:
                valid = False

    if valid:
        total += index + 1

print(total)

# 12 red cubes, 13 green cubes, and 14 blue cubes