import turtle, random, time

STEP = 20
TIMEOUT = 0.5
WIDTH = 800
HEIGHT = 600

def go_up():
    head.setheading(90)
    
def go_down():
    head.setheading(270)
    
def go_left():
    head.setheading(180)
    
def go_right():
    head.setheading(0)
    

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
            x, y = element.position()
            x = x//1
            y = y//1
        to = head.heading()
        to = to//1
        if to == 0:
            x-=STEP
        elif to == 90:
            y-=STEP
        elif to == 180:
            x+=STEP
        else:
            y+=STEP
        segment.goto(x, y)
        segment.setheading(to)
        
        snail.append(segment)
        x = STEP * random.randint(-WIDTH//(2*STEP), WIDTH//(2*STEP))
        y = STEP * random.randint(-HEIGHT//(2*STEP), HEIGHT//(2*STEP))
        food.goto(x, y)
    to = head.heading()
    to = to//1
    if to == 0:
        fx = x - STEP
        fy = y
    elif to == 90:
        fy = y - STEP
        fx = x
    elif to == 180:
        fx = x + STEP
        fy = y
    else:
        fy = y + STEP
        fx = x
    for element in snail:
        lx, ly = element.position()
        lx = lx // 1
        ly = ly//1
        element.goto(fx, fy)
        fx, fy = lx, ly
    time.sleep(TIMEOUT)
    
    for i in range(len(snail)-1, 0, -1):
        x, y = snail[i-1].xcor(), snail[i-1].ycor()
        snail[i].goto(x,y)
    
turtle.exitonclick()
