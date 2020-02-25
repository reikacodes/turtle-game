import turtle
import random



print("Hello! Welcome to the Turtle Game!")
print("The objective of this one-player game is to score as many points possible by chasing after the red target.")
print("Here are the Rules: You cannot go outside of the screen or touch the other random barriers!")
print("Each time you do, the game is instantly over, your score resets to 0, and another barrier will be added, making the game a little trickier!")
print("Aim to beat your previous score! And most importantly have fun!!!")
print("          ")

#using Turtle to set up the screen of game, player (user),target (red circle), and the scoreboard

screen = turtle.Screen()
width=500
height = 500
screen.setup(width,height)
screen.title("The Turtle Game")
screen.bgcolor("white")

player = turtle.Turtle() 
player.color("black")
player.shape("turtle")
player.pu()

target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.pu()
target.speed(0)
target.goto(-120,50)
target.shapesize(1,1,1)

score1 = turtle.Turtle()
score1.color("black")
score1.pu()
score1.hideturtle()
score1.goto(-100,230)
score1.write("Score: 0 Highest Score: 0",font = ("Gotham Book",14,"bold"))

position = []

def checkposition(x,y):
    #signature: int -> boolean
    #checks whether the coordinates of the barriers/shapes
    #overlap with the coordinates of the target
    for coordinate in position:
        if 0 < x - coordinate[0] < 25 and 0 < y - coordinate[1] < 25:
            return False

    return True

def barrier(shape,color):
    #signature: str -> int
    #if the coordinates of the barriers overlap with the target, the coordinates
    #of the barriers will be randomly reassigned
    x,y = (random.randint(-230,230),random.randint(-230,230))
    while not checkposition(x,y):
        x,y = (random.randint(-230,230),random.randint(-230,230))
       
    barrier = turtle.Turtle()
    barrier.speed(5)
    barrier.shape(shape)
    barrier.color(color)
    barrier.pu()
    barrier.goto(x,y)

    position.append((x,y))

#a list of different colors/shapes that the barrier can have
shapes = ['square','triangle','circle']
colors = ['orange','purple','green','blue',"pink"]
for i in range(3):
    barrier(random.choice(shapes), random.choice(colors))
direction = "right"
 
movement = "right"
previous = "right"

def direction(movement,previous):
    #signature: str  --> int
    #as the player is constantly moving, it changes the direction it moves by taking note of the previous direction and changing it by certain degrees to get the desired direction
    if movement == previous:
        player.rt(0)
    elif (movement == "left" and previous == "right") or (movement == "right" and previous == "left") or (movement == "down" and previous == "up") or (movement == "up" and previous == "down"):
        player.rt(180)
    elif (movement =="up" and previous == "right") or (movement == "left" and previous =="up") or (movement == "down" and previous == "left") or (movement == "right" and previous == "down"):
        player.lt(90)
    elif (movement =="up" and previous == "left") or (movement == "right" and previous =="up") or (movement == "left" and previous == "down") or (movement == "down" and previous == "right"):
        player.rt(90)

def up():
    #signature: int -> int
    #moves the y-coordinates of player upward/positive
    global movement,previous
    player.sety(player.ycor() + 25)
    direction("up",previous)
    previous = "up"
    
 
def down():
    #signature: int -> int
    #moves the y-coordinate of player downward/negative
    global movement, previous
    player.sety(player.ycor() - 25)
    direction("down",previous)
    previous = "down"
    
def right():
    #signature: int -> int
    #moves the x-coordinate of player to the right/positive
    global movement,previous
    player.setx(player.xcor() + 25)
    direction("right",previous)
    previous = "right"
    

def left():
    #signature: int -> int
    #moves the x-coordinate of player to the left/negative
    global movement,previous
    player.setx(player.xcor() - 25)
    direction("left",previous)
    previous = "left"

     
def game():
    #signature: str -> str
    #while the player moves within the boundary and avoid the barriers, the player lives.
    #to gain points, the player must chase after the red target while the scoreboard keeps both the current and highest score
    global direction

    score = 0
    highest_score = 0
    print("The game has started! You are represented by the Black Turtle! Go after the Red Target while avoiding the random shapes and going outside the boundary!")
    print("Press the keys w,s,d,a (up,down,right,left) to move around!")

    screen.onkey(up,"w")
    screen.onkey(down,"s")
    screen.onkey(left,"a")
    screen.onkey(right,"d")
    screen.listen()
    while True:
        
            
        player.fd(2.6)
        if (player.xcor() < -230 or player.xcor() > 230) or (player.ycor() < -230 or player.ycor() > 230):
            score = 0
            score1.clear()
            score1.write("Score: 0 Highest Score: "+str(highest_score),font = ("Gotham Book",14,"bold"))
            player.goto(0,0)
            
            print("Game Over!")

            stop = input("Would you like to continue the game? (y or n) ").lower()
            if stop == "n":
                exit()
            else:
                print('click on the game...')
                pass #caution: as soon as you type "y", you must immediately resume to the game screen and click on it to continue
                
            def barrier(shape,color):
                #signature: str -> int
                #if the coordinates of the barriers overlap with the target, the coordinates
                #of the barriers will be randomly reassigned
                x,y = (random.randint(-230,230),random.randint(-230,230))
                while not checkposition(x,y):
                    x,y = (random.randint(-230,230),random.randint(-230,230))
                       
                barrier = turtle.Turtle()
                barrier.speed(5)
                barrier.shape(shape)
                barrier.color(color)
                barrier.pu()
                barrier.goto(x,y)

                position.append((x,y))

            #a list of different colors/shapes that the barrier can have
            shapes = ['square','triangle','circle']
            colors = ['orange','purple','green','blue',"pink"]
            for i in range(1):
                barrier(random.choice(shapes), random.choice(colors))
            

        for coordinate in position: #between player and barrier
            if -5 < player.xcor() - coordinate[0] < 5 and -5 < player.ycor() - coordinate[1] < 5:
                score = 0
                score1.clear()
                player.goto(0,0)
                score1.clear()
                score1.write("Score: 0 Highest Score: "+str(highest_score),font = ("Gotham Book",14,"bold"))

                print("Game Over!")

                stop = input("Would you like to continue the game? (y or n) ").lower()
                if stop == "n":
                    exit()
                else:
                    print('click on the game...')
                    pass #caution: as soon as you type "y", you must immediately resume to the game screen and click on it to continue
                
                def barrier(shape,color):
                    #signature: str -> int
                    #if the coordinates of the barriers overlap with the target, the coordinates
                    #of the barriers will be randomly reassigned
                    x,y = (random.randint(-230,230),random.randint(-230,230))
                    while not checkposition(x,y):
                        x,y = (random.randint(-230,230),random.randint(-230,230))
                       
                    barrier = turtle.Turtle()
                    barrier.speed(5)
                    barrier.shape(shape)
                    barrier.color(color)
                    barrier.pu()
                    barrier.goto(x,y)

                    position.append((x,y))

                #a list of different colors/shapes that the barrier can have
                shapes = ['square','triangle','circle']
                colors = ['orange','purple','green','blue',"pink"]
                for i in range(1):
                    barrier(random.choice(shapes), random.choice(colors))
        
            
        if -10 < player.xcor() - target.xcor() < 10 and -10 < player.ycor() - target.ycor() < 10:
            target.goto(random.randint(-230,230), random.randint(-230,230))
        
            score += 10
            while score > highest_score:
                highest_score = score
                

            score1.clear()
            score1.write("Score: " + str(score) + " Highest Score: " + str(highest_score), font = ("Gotham Book",14,"bold"))

       


game()


