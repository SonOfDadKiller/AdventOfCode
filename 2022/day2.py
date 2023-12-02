input = open('strategy.txt').read().strip()

total = 0

for line in input.split('\n'):
    moves = line.split(' ')
    theirMove = 0
    for d, val in enumerate(['A', 'B', 'C']):
        if moves[0] == val:
            theirMove = d
            break
    
    myMove = 0
    for e, val in enumerate(['X', 'Y', 'Z']):
        if moves[1] == val:
            if e == 0:
                myMove = (theirMove - 1) % 3
            elif e == 1:
                myMove = theirMove
            else:
                myMove = (theirMove + 1) % 3
            
            break
    
    total += myMove + 1

    if myMove == (theirMove + 1) % 3:
        total += 6
    else: 
        if myMove == theirMove:
            total += 3

print(total)
