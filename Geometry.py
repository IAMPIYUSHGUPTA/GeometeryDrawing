number=int(input("Enter a size :"))


def geometry(x):
    z=(x*1.7)
    a1=(x//3)
    a2=(x//1.5)
    import turtle
    t=turtle.Pen()
    t.color(0,0,0)
    t.left(45)
    for i in range(0,4):
        t.left(90)
        t.forward(x)
    t.right(45)
    t.up()
    t.forward(a1)
    t.left(90)
    t.down()
    t.circle(x)
    t.right(90)
    t.up()
    t.forward(a2)
    t.down()
    t.left(60)
    for i in range(0,6):
        t.left(60)
        t.forward(z)
geometry(number)
