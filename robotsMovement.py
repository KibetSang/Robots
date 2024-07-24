# Welcome to Reeborg's world!
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def robot_move():
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
for jumps in range(6):
        robot_move()
