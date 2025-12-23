import turtle as t

t.tracer(0)
t.screensize(5000, 5000)
k = 20

t.pd()
for _ in range(7):
    t.fd(10 * k)
    for _ in range(4):
        t.circle(-2 * k, 180)
        t.rt(180)
    t.bk(10 * k)
    for _ in range(4):
        t.circle(2 * k, -180)
        t.rt(180)
t.pu()

for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * k, y * k)
        t.dot(5, 'blue')
t.goto(0, 0)
t.dot(5, 'red')
t.done()

# 39*4+3*9
