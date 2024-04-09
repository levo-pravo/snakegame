import turtle, random, time

STEP = 20
TIMEOUT = 0.2
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
count = 0

pen = turtle.Turtle()
pen.pu()
pen.color("white")
pen.hideturtle()
pen.goto(0, 0)
#pen.write(f"Счет: {count}", font=("Arial", 40, "bold"))

while True:
    if head.distance(food) < 2:
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.penup()
        segment.color("light blue")
        snail.append(segment)
        x = STEP * random.randint(-WIDTH//(2*STEP), WIDTH//(2*STEP))
        y = STEP * random.randint(-HEIGHT//(2*STEP), HEIGHT//(2*STEP))
        food.goto(x, y)
        count+=1
        
    if head.xcor() > WIDTH//2 or head.xcor() < -WIDTH//2 or head.ycor() > HEIGHT//2 or head.ycor() < -HEIGHT//2:
        break
        
    for i in range(len(snail)-1, 0, -1):
        x, y = snail[i-1].xcor(), snail[i-1].ycor()
        snail[i].goto(x,y)
    
    head.forward(STEP)
    time.sleep(TIMEOUT)
    
pen.write(f"Счет: {count}", font=("Arial", 40, "bold"))
turtle.exitonclick()
