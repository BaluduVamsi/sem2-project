p = {}
while True:
    n = input("Enter p name (done to stop): ")
    if n.lower() == 'done':
        break
    v = float(input(f"Enter price for {n}: "))
    p[n] = v

while True:
    s = input("Enter p name (exit to stop): ")
    if s.lower() == 'exit':
        break
    print(f"Price: {p[s]}" if s in p else "Not found")