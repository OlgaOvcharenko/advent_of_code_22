import os
import string

test_1 = 0
f = open('input3.txt', 'r')
rucksacks = [line.split('\n')[0] for line in f.readlines()]

letters = list(string.ascii_lowercase)
letters.extend(string.ascii_uppercase)

priorities = dict(zip(letters, range(1, 53)))

if test_1:
    pr_sum = 0
    for rucksack in rucksacks:
        half = int(len(rucksack) / 2)
        r1, r2 = set(rucksack[0:half]), set(rucksack[half:])
        both_item = r1.intersection(r2).pop()
        pr_sum += priorities[both_item]

else:
    pr_sum = 0
    for i in range(0, len(rucksacks), 3):
        r1, r2, r3 = set(rucksacks[i]), set(rucksacks[i+1]), set(rucksacks[i+2])
        both_item = r1.intersection(r2).intersection(r3).pop()
        pr_sum += priorities[both_item]

    print(pr_sum)
