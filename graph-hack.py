import subprocess
import os
#call(['echo "Hello"'])

pattern = open('pattern.txt', 'r')

pattern_list = []

colors = []

for line in pattern:
    if line[0] == '#':
        pass

    elif line[0] == 'm':
        commit_multiply = int(line[2:-1])
        print(commit_multiply)

    elif line[0] == '1':
        colors.append(line[2])

    elif line[0] == '2':
        colors.append(line[2])

    elif line[0] == '3':
        colors.append(line[2])

    elif line[0] == '4':
        colors.append(line[2])

    elif line[0] == '5':
        colors.append(line[2])

    elif line[0] == '@':
        for i in range(2, len(line[0:-1])):
            pattern_list.append(line[i])
    else:
        pass

# Sort list in the order that commits need to be pushed
weeks_in_order = []
for i in range(0, 53):
    week = i
    for j in range(0, 7):

        if pattern_list[0 + week] == colors[0]:
            weeks_in_order.append(str(0 ** commit_multiply))

        elif pattern_list[0 + week] == colors[1]:
            weeks_in_order.append(str(1 ** commit_multiply))

        elif pattern_list[0 + week] == colors[2]:
            weeks_in_order.append(str(2 ** commit_multiply))

        elif pattern_list[0 + week] == colors[3]:
            weeks_in_order.append(str(3 ** commit_multiply))

        elif pattern_list[0 + week] == colors[4]:
            weeks_in_order.append(str(4 ** commit_multiply))

        else:
            weeks_in_order.append(str(0 * commit_multiply))

        week += 53

os.putenv('COMMITS', ' '.join(weeks_in_order))

subprocess.call('./graph-hack.sh')