from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
bat_y = 4
ball_position = [3, 3]
ball_velocity = [1, 1] 
def start_game():
  level_time=ask_level()
  while True:
    sense.clear(0, 0, 0)
    draw_ball()
    draw_bat()
    sleep(level_time)

def ask_level():
  print("Welcome to  Pong 9.0\nPress 1 for Easy\nPress 2 for Medium\nPress 3 for Hard\nPress 4 to quit")
  level=int(input('enter the level of difficulty:'))
  if level==1:
    return 0.5
  elif level==2:
    return 0.25
  elif level==3:
    return 0.20
  elif level==4:
    quit()
  else:
    print("Invalid Input")
    start_game()

def draw_bat():
    sense.set_pixel(0, bat_y, 0, 255, 255)
    sense.set_pixel(0, bat_y+1, 0, 255, 255)
    sense.set_pixel(0, bat_y-1, 0, 255, 255)

def move_up(event):
    global bat_y
    if bat_y > 1 and event.action=='pressed':
        bat_y -= 1
def move_down(event):
    global bat_y
    if bat_y < 6 and event.action=='pressed':
        bat_y += 1
  

def draw_ball():
    sense.set_pixel(ball_position[0], ball_position[1], 255, 0, 255)
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[0] == 7:
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[1] == 0 or ball_position[1] == 7:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 0:
        sense.show_message("You Lose", text_colour=(255, 0, 0))
        ball_position[0] = 3
        ball_position[1]=3
        ball_velocity[1] = 1
        ball_velocity[0]=1
        start_game()
    if ball_position[0] == 1 and bat_y - 1 <= ball_position[1] <= bat_y+1:
        ball_velocity[0] = -ball_velocity[0]
      
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

start_game()
