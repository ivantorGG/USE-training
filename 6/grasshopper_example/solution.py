def re_color():
    global colored
    if colored.get(pos):
        del colored[pos]
    else:
        colored[pos] = 1


colored = {}
pos = 0

for _ in range(7):
    for _ in range(2):
        pos += 3

    re_color()
    pos -= 4
    re_color()

print(len(colored))
