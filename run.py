import time, redis

redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 128
PADDLE_HEIGHT = 16

while True:
  # Get variables
  px = int(redis_db.get('ball_pos_x'))
  py = int(redis_db.get('ball_pos_y'))
  vx = int(redis_db.get('ball_vel_x'))
  vy = int(redis_db.get('ball_vel_y'))
  
  left_paddle_x = int(redis_db.get('left_paddle_x'))
  left_paddle_y = int(redis_db.get('left_paddle_y'))
  left_paddle_movement = int(redis_db.get('left_paddle_movement'))
  left_paddle_score = int(redis_db.get('left_paddle_score'))

  right_paddle_x = int(redis_db.get('right_paddle_x'))
  right_paddle_y = int(redis_db.get('right_paddle_y'))
  right_paddle_movement = int(redis_db.get('right_paddle_movement'))
  right_paddle_score = int(redis_db.get('right_paddle_score'))
  
  loops = int(redis_db.get('loops'))
  
  # Move the left paddle
  left_paddle_y += left_paddle_movement * 2
  if(left_paddle_y < 0): left_paddle_y = 0
  if(left_paddle_y + PADDLE_HEIGHT > SCREEN_HEIGHT): left_paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT
  
  # Move the right paddle
  right_paddle_y += right_paddle_movement * 2
  if(right_paddle_y < 0): right_paddle_y = 0
  if(right_paddle_y + PADDLE_HEIGHT > SCREEN_HEIGHT): right_paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT
  
  bounced = 0
  # Bounce the ball off the paddle
  if(px == left_paddle_x+1):
    if(py >= left_paddle_y and py <= left_paddle_y+PADDLE_HEIGHT):
      vx = 1
      bounced = 1
  if(px == right_paddle_x-1):
    if(py >= right_paddle_y and py <= right_paddle_y+PADDLE_HEIGHT):
      vx = -1
      bounced = 1
  
  # Bounce the ball off the edges of the screen
  if px >= SCREEN_WIDTH: 
    vx = -1
    left_paddle_score += 1
  if px <= 0: 
    vx = 1
    right_paddle_score += 1
  if py >= SCREEN_HEIGHT: vy = -1
  if py <= 0: vy = 1
  
  # Reset if needed, otherwise move the ball
  if(left_paddle_score >= 3 or right_paddle_score >= 3):
    px = SCREEN_WIDTH/2
    py = SCREEN_HEIGHT/2
  else:
    px += vx
    py += vy

  # Save variables
  loops += 1
  
  redis_db.set('loops', str(loops))
  
  redis_db.set('ball_pos_x', str(px))
  redis_db.set('ball_pos_y', str(py))
  redis_db.set('ball_vel_x', str(vx))
  redis_db.set('ball_vel_y', str(vy))
  redis_db.set('ball_bounced', bounced)

  redis_db.set('left_paddle_y', left_paddle_y)
  redis_db.set('left_paddle_score', left_paddle_score)
  
  redis_db.set('right_paddle_y', right_paddle_y)
  redis_db.set('right_paddle_score', right_paddle_score)

  time.sleep( 1.0 / (20.0 + (loops/300)) )
