import random
import turtle as t
t.bgcolor('yellow')
caterpillar = t.turtles()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()
leaf = t.turtles()
leaf_shape = (0, 0), (14, 2), (18, 6), (20, 20),  (6, 18), (2, 14)
t.register_shape('leaf'), leaf_shape
leaf_shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)
caterpillar = t.turtles()
caterpillar. shape('square')
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
leaf.hideturtle
leaf.speed(0)
game_stared = False
text_turtle = t.turtle()
text_turtle.write('PRESS SPACE to to start', align = 'center', font ('Arial', 16, 'bold')
score_turtle = t.turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def start_game():
    global game_started
if game_stared:
    return
game_started = True
score = 0
text_turle.clear()
caterpillar_speed = 2
caterpillar_length = 3
caterpillar_shapesize(1, caterpillar_length, 1)
caterpillar.showturtle()
caterpillar.showturtle()
display_score(score)
place_leaf


while True:
    caterpillar.foward(caterpillar_speed)
    if caterpillar.distance.(leaf) < 20:
    place_leaf
    caterpillar_length = caterpillar_length + 1
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar_speed = caterpillar_speed + 1
    score = score + 10
    display_score(score)
if outside_window():
    game_over()





