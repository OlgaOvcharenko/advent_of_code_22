import os
test_1 = 0
f = open('input2.txt', 'r')
games = [line.replace('\n', '').split(' ') for line in f.readlines()]

instrument_points = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}
winning_strategies = {'X': 'C', 'Z': 'B', 'Y': 'A', 'C': 'X', 'B': 'Z', 'A': 'Y'}
draw_strategies = {'X': 'A', 'Z': 'C', 'Y': 'B', 'A': 'X', 'C': 'Z', 'B': 'Y'}

win_lose_points = {'X': 0, 'Y': 3, 'Z': 6}

if test_1:
    points = 0
    for game in games:
        points += instrument_points[game[1]]
        if game[0] == draw_strategies[game[1]]:
            points += 3

        elif winning_strategies[game[1]] == game[0]:
            points += 6

        else:
            points += 0

else:
    points = 0
    for game in games:
        points += win_lose_points[game[1]]

        if game[1] == 'Z':
            points += instrument_points[winning_strategies[game[0]]]

        elif game[1] == 'Y':
            points += instrument_points[game[0]]

        else:
            instrument = set(win_lose_points.keys()) \
                .difference({draw_strategies[game[0]], winning_strategies[game[0]]})
            points += instrument_points[instrument.pop()]

print(points)
