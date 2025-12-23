import turtle as t


t.tracer(0)
t.screensize(3000, 3000)
k = 20


t.pd()
for _ in range(5):
    t.forward(37 * k)
    t.right(90)
    t.forward(44 * k)
    t.right(90)
t.pu()

t.backward(18 * k)
t.right(90)
t.forward(29 * k)
t.left(90)

t.pd()
for _ in range(5):
    t.forward(31 * k)
    t.right(90)
    t.forward(35 * k)
    t.right(90)
t.pu()


for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * k, y * k)
        t.dot(5)
t.goto(0, 0)
t.dot(5, 'red')

t.done()

# 16*14
