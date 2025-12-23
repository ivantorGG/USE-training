import turtle as t


t.tracer(0)
t.screensize(3000, 3000)
k = 15
t.right(90)


t.pd()
for _ in range(3):
    t.forward(39 * k)
    t.right(90)
    t.forward(48 * k)
    t.right(90)
t.pu()

t.forward(27 * k)
t.right(90)
t.forward(24 * k)
t.left(90)

t.pd()
for _ in range(3):
    t.forward(29 * k)
    t.right(90)
    t.backward(18 * k)
    t.right(90)
t.pu()


for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * k, y * k)
        t.dot(5)

t.done()

# 39*48+29*18-12*18
