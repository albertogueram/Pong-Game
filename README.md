## Paddle Class
#### Up, Right:
Change the heading of the paddle

## Ball Class
Inheritance of Turtle class from turtle package
#### Move:
Takes new x,y adding the moving attributes defines in the initialization
#### Bounce_x & Bounce_y:
When the ball collision a paddle or an edge it
reverts the x or y direction
#### Point:
When some paddle achive a goal it reset the position of the ball

## ScoreBoard Class 
Inheritance of Turtle class from turtle package
#### Refresh:
Update the score and call update_scoreboard method
whenever some paddle achieve a goal

# Main Function
a) Set up the screen
b) Create the paddles
c) Detects movement of the paddles
d) While loop until detects of game over
d.1) Call bounce_y method if ball collision with an edge
d.2) Call bounce_x method if ball collision with a paddle
d.3) Increase speed
d.4) Increase score of the gamers 
d.5) Check if somebody reach 3 points