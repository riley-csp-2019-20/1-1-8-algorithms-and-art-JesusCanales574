import turtle as trtl
joe = trtl.Turtle()
joe.speed(0)
joe.fillcolor("black")

# first make the road
joe.begin_fill()
joe.penup()
joe.goto(-475,-200)
joe.pendown()

joe.goto(470,-200)

joe.right(90)
joe.forward(150)
joe.right(90)
joe.goto(-475,-350)

joe.right(90)
joe.goto(-475,-200)
joe.end_fill()

# make the yellow lines on the road
x = -400
y = -275
for i in range(6):
    joe.penup()
    joe.goto(x,y)
    joe.pendown()

    joe.fillcolor("yellow")
    joe.begin_fill()
    joe.forward(10)
    joe.right(180)
    joe.forward(20)
    joe.left(90)
    joe.forward(100)
    joe.left(90)
    joe.forward(20)
    joe.left(90)
    joe.forward(100)
    joe.end_fill()

    joe.penup()
    x = x + 140
    joe.right(90)
    joe.pendown()

# make the sidewalk
joe.penup()
joe.goto(-475,-100)
joe.pendown()

joe.fillcolor("gray")
joe.begin_fill()
joe.right(90)
joe.goto(470,-100)
joe.right(90)
joe.goto(470,-200)
joe.right(90)
joe.goto(-475,-200)
joe.right(90)
joe.goto(-475,-100)
joe.end_fill()

# Make the house
joe.goto(-175,-100)
joe.pencolor("brown")
joe.pensize(6)
joe.forward(500)
joe.right(90)
joe.forward(400)
joe.right(90)
joe.forward(500)
joe.right(90)
joe.forward(400)




wn = trtl.Screen()
wn.mainloop()