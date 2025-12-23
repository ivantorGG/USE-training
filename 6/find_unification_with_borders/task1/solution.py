import turtle as t


t.tracer(0)
t.screensize(1000, 1000)
k = 20


t.pd()
for _ in range(2):
    t.forward(14 * k)
    t.left(270)
    t.backward(12 * k)
    t.right(90)
t.pu()

t.forward(9 * k)
t.right(90)
t.backward(7 * k)
t.left(90)

t.pd()
for _ in range(2):
    t.forward(13 * k)
    t.right(90)
    t.forward(6 * k)
    t.right(90)
t.pu()


for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * k, y * k)
        t.dot(5)
t.goto(0, 0)
t.dot(5, 'red')

t.done()

# 15*13+14*7-6*7
