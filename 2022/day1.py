
file = open('calories.txt', 'r')
elfCalories = [0]

for line in file.readlines():
    if line != "\n":
        elfCalories[-1] += int(line)
    else:
        elfCalories.append(0)

elfCalories.sort()

print(elfCalories[-1], end="\n\n")
print(elfCalories[-1] + elfCalories[-2] + elfCalories[-3])
