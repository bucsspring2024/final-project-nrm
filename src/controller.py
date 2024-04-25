import pygame
import os

from src.history import History
from src.math import Math
from src.lunch import Lunch
from src.gym import Gym
from src.end_of_day import EndDay

class Controller:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Wake up! It's time for school!")
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, "assets", "alarmclock.png")
        self.alarmclock_image = pygame.image.load(image_path)
        #ring an alarm sound
        

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        


# import pygame

# class Controller:
#     def __init__(self):
#         pygame.init()
#         self.width = 800
#         self.height = 800
#         self.screen = pygame.display.set_mode((self.width, self.height))
#         pygame.display.set_caption("Wake up! It's time for school!")
#         self.alarmclock_image = pygame.image.load("/Users/lilyaronov/github-classroom/bucsspring2024/final-project-nrm/assets/alarmclock.png")

#     def mainloop():
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     exit()

# import pygame

# class Controller:
#     def __init__(self):
#         pygame.init()
#         self.screen_width = 800
#         self.screen_height = 600
#         self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
#         pygame.display.set_caption("My Pygame Application")
#         self.clock = pygame.time.Clock()
#         self.is_running = False
        
# __name__ == "__main__"



# import pygame
# class Controller:
  
#   def __init__(self):
#     pygame.init()
    
    
#   def mainloop(self):
#     #select state loop
    
  
#   ### below are some sample loop states ###

#   def menuloop(self):
#       #event loop

#       #update data

#       #redraw
      
#   def gameloop(self):
#       #event loop

#       #update data

#       #redraw
    
#   def gameoverloop(self):
#       #event loop

#       #update data

#       #redraw
