from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
import time


# Screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# Snake object
snake = Snake()

# Food object
food = Food()

# Scoreboard object
scoreboard = ScoreBoard()

# Listen to keystrokes (BELOW CODES ARE USED TO CONTROL SNAKE MOVEMENTS IN UP,DOWN,LEFT,RIGHT USING ARROW KEYS IN KEYBOARD)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food ( we will use distance method in turtle class = turtle.distance )
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend_length()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail (concept of slicing we have used)
    # Slicing and tuple concept is used where [1:] defines all elements in list except 1st one
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()

#Refrence code :-

#THE BELOW CODE IS THE CODE FOR THE MAKING OF THE BODY OF THE SNAKE WITH THE HELP OF 3 PARTS (SEGMENTS) :-
# segment_1 = Turtle("square")
# segment_1.color("white")

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(x=-20,y=0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(x=-40,y=0)

# tHIS CODE IS THE EASY FORM OF ABOVE CODE IN TERMS OF "FOR LOOP"
# start_positions = [(0,0),(-20,0),(-40,0)]
# segments = []
# for positions in start_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(positions)
#     segments.append(new_segment)


# for seg in segments:
#    seg.forward(20)
# segments[0].left(90)

#tHE BELOW CODE IS FOR JOINING THE 3 SEGMENTS IN 1 COMBINED SNAKE SO THAT IT DOESN'T BREAK DURING THE MOVEMENT :-
# for segment_number in range(len(segments)-1,0,-1):
#     new_x =segments[segment_number-1].xcor()
#     new_y = segments[segment_number - 1].ycor()
#     segments[segment_number].goto(new_y,new_x)
# segments[0].forward(20)
# segments[0].left(90)
#