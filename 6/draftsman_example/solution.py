import turtle as t

t.tracer(0)
t.screensize(5000, 5000)
k = 20

x, y = 0, 0
for _ in range(10):
    t.pu()
    y += 2
    t.pd()
    t.goto(x * k, y * k)

    t.pu()
    x += 2
    t.pd()
    t.goto(x * k, y * k)

    t.pu()
    y += 10
    t.pd()
    t.goto(x * k, y * k)

    t.pu()
    x += -2
    t.pd()
    t.goto(x * k, y * k)

    t.pu()
    y += 2
    t.pd()
    t.goto(x * k, y * k)

    t.pu()
    x += 6
    t.pd()
    t.goto(x * k, y * k)

    t.pu()
    y += -2
    t.pd()
    t.goto(x * k, y * k)

    t.pu()
    x += -2
    t.pd()
    t.goto(x * k, y * k)

    t.pu()
    y += -10
    t.pd()
    t.goto(x * k, y * k)

    t.pu()
    x += 2
    t.pd()
    t.goto(x * k, y * k)

    t.pu()
    y += -2
    t.pd()
    t.goto(x * k, y * k)

    t.pu()
    x += -6
    t.pd()
    t.goto(x * k, y * k)


t.pu()

for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * k, y * k)
        t.dot(5, 'blue')
t.goto(0, 0)
t.dot(5, 'red')
t.done()

# 69
