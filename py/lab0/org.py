orangecaps = {'test1': {'Dhoni': 74, 'kohil': 150}, 'test2': {'Dhoni': 29, 'Sachin': 143}}
scores = {}
for test in orangecaps:
    for player, runs in orangecaps[test].items():

        if player not in scores:
          scores[player] =0
        scores[player] = scores.get(player) + runs
winner = max(scores, key=scores.get)
print(winner, scores[winner])