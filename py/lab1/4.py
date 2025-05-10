p = [[], [], [], [], []]
for number in range(1, 10001):
    p[number % 5].append(number)

u = list(range(1, 10001))
all_numbers = []
for remainder in p:
    for num in remainder:
        all_numbers.append(num)

if sorted(all_numbers) == sorted(u):
    print("Valid.")

for r, n in enumerate(p):
    print(f"Remainder {r}: {n[:10]} ...")