from turtle import Turtle, Screen
playerSpeed = 30

#def moveLeft():
 #   x = timmy.xcor - playerSpeed

  #  if x > 0 

timmy = Turtle()
#print(timmy)

timmy.shape("turtle")
timmy.color("coral")
timmy.penup()
#timmy.forward(100)
#timmy.sety(100)
timmy.setposition(100,100)

timmy.setposition(200,200)
timmy.pendown()
timmy.setposition(100,100)

#timmy.

my_screen = Screen()
print(timmy.pos())
print(my_screen.window_width())
my_screen.exitonclick()