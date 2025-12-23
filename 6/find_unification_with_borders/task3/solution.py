import turtle


turtle.tracer(0)
turtle.screensize(4000, 4000)
k = 20


turtle.pd()
for _ in range(2):
    turtle.forward(20 * k)
    turtle.left(270)
    turtle.forward(12 * k)
    turtle.right(90)
turtle.pu()

turtle.forward(9 * k)
turtle.right(90)
turtle.forward(7 * k)
turtle.left(90)

turtle.pd()
for _ in range(2):
    turtle.forward(13 * k)
    turtle.right(90)
    turtle.forward(6 * k)
    turtle.right(90)
turtle.pu()


for x in range(-50, 50):
    for y in range(-50, 50):
        turtle.goto(x * k, y * k)
        turtle.dot(5, 'darkred')
turtle.goto(0, 0)
turtle.dot(5, 'blue')

turtle.done()

# 13*21+2*7+12
