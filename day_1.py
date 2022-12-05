import os

f = open('input1.txt', 'r')
calories_per_elf = [sum([int(calory) for calory in line.split('\n') if calory.isdigit()])
            for line in f.read().split('\n\n')]
calories_per_elf.sort(reverse=True)
top_3 = calories_per_elf[:3]
print(sum(top_3))
