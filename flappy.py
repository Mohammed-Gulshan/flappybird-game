import pygame
from pygame.locals import*
import random

pipes_list=['assets/greenpipe.png']
pipe_sur=pygame.image.load(random.choice(pipes_list))
pipes_list2=[]
show_pipe=pygame.USEREVENT
pipe_heights=[200,250,350]

pygame.init()
pygame.time.set_timer(show_pipe,800)
display_width=288
display_height=384
gravity=0.2
bird_movement=0
game_on=True

game_display=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('flappy bird game clone')
speed=pygame.time.Clock()
back_ground=pygame.image.load('assets/bgday.png').convert()
base=pygame.image.load('assets/base.png').convert()
base_x_pos = 0

bird_surf=pygame.image.load('assets/bird3.png')
bird_rectangle=bird_surf.get_rect(center=(25,255))

def base_move():
  game_display.blit(base,(base_x_pos,310))
  game_display.blit(base,(base_x_pos +288,310))

def adding_pipes():
  random_pipe_height=random.choice(pipe_heights)
  base_pipe=pipe_sur.get_rect(midbottom=(288,random_pipe_height-150))
  top_pipe=pipe_sur.get_rect(midtop=(288,random_pipe_height))

  return base_pipe,top_pipe

def pipes_move(pipes):
  for pipe in pipes:
      pipe.centerx -=5
  return pipes  

def show_pipes(pipes):
  for pipe in pipes:
    if pipe.bottom >= 384:
      game_display.blit(pipe_sur,pipe)
    else: 
      reverse_pipe=pygame.transform.flip(pipe_sur,False,True)
      game_display.blit(reverse_pipe,pipe)

def collision(pipes):
  for pipe in pipes:
    if bird_rectangle.colliderect(pipe):
      return False

  if bird_rectangle.top <=-25 or bird_rectangle.bottom >= 310:
    return False

  return True
  
while True:
  for event in pygame.event.get():
    if event.type==QUIT or (
      event.type==KEYDOWN and(
        event.key==K_ESCAPE or 
        event.key==K_q)):
        pygame.quit()
        quit()

    elif event.type==pygame.KEYDOWN and game_on==True:
      if event.key==pygame.K_SPACE:
        bird_movement=0
        bird_movement -=8.5

    elif event.type==pygame.KEYDOWN and game_on==True:
      if event.key==pygame.K_SPACE:
        pipes_list2.clear()
        game_on=True
        bird_movement=0
        bird_rectangle.center(-25 ,255)
   
    if event.type==show_pipe:
        pipes_list2.extend(adding_pipes())

   

  speed.tick(80)
  game_display.blit(back_ground,(0,0))
  
  if game_on:
    bird_movement+=gravity
    bird_rectangle.centery+=bird_movement
    game_display.blit(base,(0,310))
    game_display.blit(bird_surf,bird_rectangle)
    game_on=collision(pipes_list2)
    pipes_list2=pipes_move(pipes_list2)
    show_pipes(pipes_list2) 

  pygame.display.update()
  
  base_move()
  base_x_pos -= 1

  if base_x_pos <= -288:
    base_x_pos=0
  
  
  
     
  