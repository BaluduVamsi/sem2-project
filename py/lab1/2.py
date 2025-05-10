import random
a = [random.randint(0, 1) for _ in range(100)]
longestrun = 0
currentrun = 0
for num in a:
    if num == 0:
        currentrun += 1
        longestrun= max(longestrun, currentrun)
    else:
        currentrun = 0
print("Random integers:", a)
print("Longest run of zeros:", longestrun)