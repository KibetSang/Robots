# Welcome to Reeborg's world!

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
