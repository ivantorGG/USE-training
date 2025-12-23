import turtle as t


t.tracer(0)
t.screensize(1000, 1000)
k = 20


t.pd()
for _ in range(2):
    t.forward(3 * k)
    t.right(90)
    t.forward(20 * k)
    t.right(90)
t.pu()

t.backward(8 * k)
t.right(90)
t.forward(9 * k)
t.left(90)

t.pd()
for _ in range(2):
    t.forward(16 * k)
    t.right(90)
    t.forward(8 * k)
    t.right(90)
t.pu()


for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * k, y * k)
        t.dot(5, 'blue')
t.goto(0, 0)
t.dot(5, 'red')

t.done()

# 17*9+12+36
