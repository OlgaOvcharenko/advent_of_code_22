import os
import string

test_1 = 0
f = open('input4.txt', 'r')
pairs = [[[[int(pair.split('-')[0]), int(pair.split('-')[1])] for pair in pairs_line.split(',')]
              for pairs_line in line.split('\n') if pairs_line]
             for line in f]

if test_1:
    count_incl = 0
    for pair in pairs:
        a, b = pair[0][0][0], pair[0][0][1]
        c, d = pair[0][1][0], pair[0][1][1]

        if (a <= c and d <= b) or (a >= c and d >= b):
            count_incl += 1

    print(count_incl)

else:
    count_incl = 0
    for pair in pairs:
        a, b = pair[0][0][0], pair[0][0][1]
        c, d = pair[0][1][0], pair[0][1][1]

        if  (b >= c and a <= d) or (a >= d and b <= c):
            count_incl += 1

    print(count_incl)