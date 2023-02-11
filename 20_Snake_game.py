import random
import time
import turtle #graphics
delay=0.1 #we can pass sleep() of time module which produces a gap
score=0
highestScore=0
#snake bodies
#snake head-black color
#snake body-red color
bodies=[]
#getting a screen | canvas
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=600,height=600)
#creating a snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")#border color of snake head is white
head.fillcolor("blue")#filled color of snake head is blue
head.penup()#when turtle is moved and penup is used then nothing is drawn.
head.goto(0,0)#starting position of head
head.direction="stop"#stop the head at the centre
#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")#food border color
food.fillcolor("green")#food filled color
food.penup()#when turtle is moved and penup is used then nothing is drawn.
food.ht()#hide turtle
food.goto(0,200)#initial location
food.st()#show turtle
#score board
sb=turtle.Turtle()
sb.shape('square')
sb.fillcolor('black')
sb.penup()#when turtle is moved and penup is used then nothing is drawn.
sb.ht()
sb.goto(-250,-250)#position of the score apperance
sb.write("Score:0 | Highest Score: 0")#turtle has a write method which shows
# string messsage on the screen
def moveup():
    if head.direction!='down':
        head.direction='up'
def movedown():
    if head.direction!='up':
        head.direction='down'
def moveleft():
    if head.direction!='right':
        head.direction='left'
def moveright():
    if head.direction!='left':
        head.direction='right'
def movestop():
        head.direction='stop'
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)    
#Event Handling-key mappings
s.listen()
s.onkey(moveup,"up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")
#main lop
while True:
    s.update()#this is to update the screen
    #check collosion with border
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()< -290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)  
    if head.ycor()<-290:
        head.sety(290)  
    #check collosion with food
    if head.distance(food)<20:
        #move the food to new random place
        x=random.randint(-290,290) 
        y=random.randint(-290,290)
        food.goto(x,y)
        #increase the length of the snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        #append new body
        bodies.append(body)
        #increase the score
        score+=10
        #change delay
        delay=0.001
        #update the highest score
        if score>highestScore:
            highestScore=score
        sb.clear()
        sb.write("Score: {} highest Score : {}".format(score,highestScore))
       #move the snake body
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcolor()
        y=bodies[index-1].ycolor()
        bodies[index].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()
    #check collosion with snake body
    for body in bodies:
        if body.distance(head)<20:
            time.slep(1)
            head.goto(0,0)
            head.direction="stop"
            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            score=0
            dalay=0.1
            #update score board
            sb.clear()
            sb.write("Score: {} highest Score : {}".format(score,highestScore))
    time.sleep(delay)
    s.mainloop()
        
        












