import random
import turtle as t
t.bgcolor('yellow')
caterpillar = t.turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()
leaf = t.turtle()
leaf_shape = (0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14)
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)
game_started = False
text_turtle = t.turtle()
text_turtle.write('PRESS SPACE to start', align = 'center',)
text_turtle.hideturtle()
score_turtle = t.turtle()
score_turtle.hideturtle()
score_turle.speed (0)


def outside_window():


    pass
def display_score(current_score):


    def place_leaf():
        pass


def start_game() :
    while loop():
        global game_started
    if game_started:
        return
    game_started = True
    score = 0
    text_turtle.clear
    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()
while true:
    caterpillar.foward(caterpillar_speed)
    if caterpillar.distance(leaf) < 20:
        place_leaf()
        caterpillar_length = caterpillar_length + 1
        caterpillar.shapesize(1, caterpillar_length, 1)
        caterpillar_speed = caterpillar_speed + 1
        score = score + 10
        display_score(score)
    if outside_window() :
        game_over()
        t.onkey(start_game, 'space')
        t.listen
        t.mainloop()

        left_wall = t.window_width() / 2
        right_wall = t.window_width() / 2
        top_wall = t.window_height() / 2
        bottom_wall = t.window_height() / 2
        (x, y) = caterpillar.pos()
        caterpillar.color('yellow')
        leaf.color('yellow')
        t.penup()
        t.hideturtle()
        t.write('GAME OVER!',align='center', font=('Arial',30,'normal'))
        score_turtle.clear()
        score_turtle.penup()
        x = (t.window_width() / 2) - 50
        y = (t.window_height() / 2) - 50
        score_turtle.setpos(x, y)
        score_turtle.write(str(curent_score), align='right'
 def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)
def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)
def move_left():
     if caterpillar.heading() == 90 or caterpillar.heading() == 270:
         caterpillar.setheading(180)
def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() ==270: caterpillar.setheading(0)
    t.onkey(move_up, 'Up')
    t.onkey(move_right, 'Right')
    t.onkey(move_down, 'Down')
    t.onkey(move_left, 'Left')
    t.mainloop()



