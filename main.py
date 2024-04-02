import turtle, random, time

STEP = 20
TIMEOUT = 0.5
WIDTH = 800
HEIGHT = 600

def go_up():
    for element in snail:
        element.setheading(90)
    
def go_down():
    for element in snail:
        element.setheading(270)
    
def go_left():
    for element in snail:
        element.setheading(180)
    
def go_right():
    for element in snail:
        element.setheading(0)
    

screen = turtle.Screen()
screen.title('Змееныш')
screen.bgcolor('lightgreen')
screen.setup(WIDTH, HEIGHT)

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

head = turtle.Turtle()
head.penup()
head.shape('square')
head.color("blue")

snail = []
snail.append(head)

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.penup()
food.color("purple")
x = STEP * random.randint(-WIDTH//(2*STEP), WIDTH//(2*STEP))
y = STEP * random.randint(-HEIGHT//(2*STEP), HEIGHT//(2*STEP))
food.goto(x, y)

while True:
    if head.distance(food) < 2:
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.penup()
        segment.color("blue")
        for element in snail:
            x, y = element.getPos()
        snail.append(segment)
        x = STEP * random.randint(-WIDTH//(2*STEP), WIDTH//(2*STEP))
        y = STEP * random.randint(-HEIGHT//(2*STEP), HEIGHT//(2*STEP))
        food.goto(x, y)
    for element in snail:
        element.forward(STEP)
    time.sleep(TIMEOUT)
    
turtle.exitonclick()
