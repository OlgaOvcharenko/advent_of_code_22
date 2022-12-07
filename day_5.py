import queue
from collections import deque
from collections import defaultdict

test_1 = 0
f = open('input5.txt', 'r')

stacks = defaultdict(list)

len_cargo = 3
is_first_line = True

num_global_stacks = 0

# Parse stacks
for line in f:
    # Stop if reached end of containers
    if line.count('[') == 0:
        break

    num_global_stacks = int(len(line) / 4)
    if is_first_line:
        for i in range(1, num_global_stacks + 1):
            q = deque()
            stacks[i] = list()
        is_first_line = False

    # TODO Merge later
    first_stack = line[0:len_cargo].replace(' ', '').replace('\n', '').replace(',', '')
    if first_stack:
        stacks[1].append(first_stack)

    for it, idx in zip(range(2, len(stacks)+1), range(len_cargo, len(line)+1, len_cargo)):
        stack_item = line[idx+1:idx+1+1+len_cargo]
        stack_item = stack_item.replace(' ', '').replace('\n', '').replace(',', '')
        if stack_item:
            stacks[it].append(stack_item)

f.readline()
print(stacks)

for line in f:
    move, from_s, to_s = int(line.split(' ')[1]), int(line.split(' ')[3]), int(line.split(' ')[5])

    for c_i in range(move):
        stacks[to_s].insert(0, stacks[from_s].pop(0))

for s in stacks.keys():
    print(stacks[s][0])
