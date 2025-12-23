import turtle as t

t.tracer(0)
t.screensize(3000, 3000)
k = 20

t.pd()
for _ in range(10):
    t.fd(2 * k)
    t.dot(5, 'red')
    t.fd(3 * k)
    t.rt(90)
    t.fd(3 * k)
    t.lt(90)
    t.fd(1 * k)
    t.dot(5, 'red')
    t.lt(90)
    t.fd(3 * k)
    t.lt(90)

t.done()

# 4
