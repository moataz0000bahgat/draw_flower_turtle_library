import turtle
def draw_square(some_turtle):
    
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_flower(some_turtle):
    x=360/20
    for i in range(1,20):
       some_turtle.right(x)
       draw_square(some_turtle)
    some_turtle.right(120)   
    some_turtle.forward(200)
    
def draw_art():
    window=turtle.Screen()
    window.bgcolor('red')
    #create the turtle Brad -Draws a square
    brad=turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)
    draw_square(brad)
    draw_flower(brad)
    #create the turtle angie - Draws a circle
    #angie=turtle.Turtle()
    #angie.shape('arrow')
    #angie.color('blue')
    #angie.circle(100)

    
draw_art()
