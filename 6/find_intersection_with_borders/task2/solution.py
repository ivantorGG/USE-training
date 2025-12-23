import turtle as t

t.tracer(0)
t.screensize(5000, 5000)
k = 15

t.pd()
for _ in range(4):
    t.fd(50 * k)
    t.lt(90)
t.pu()

t.fd(50 * k)
t.lt(135)

t.pd()
for _ in range(2):
    t.fd(102 * k)
    t.lt(120)
    t.fd(182 * k)
    t.lt(60)
t.pu()

for x in range(-60, 120):
    for y in range(-70, 70):
        t.goto(x*k, y*k)
        t.dot(5, 'blue')
t.goto(0, 0)
t.dot(8, 'red')

t.done()

# 50*50/2
