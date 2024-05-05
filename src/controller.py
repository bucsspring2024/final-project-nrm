import pygame
from src.history import History
from src.math_1 import Math
from src.lunch import Lunch
from src.end_of_day import End

class Controller():
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Wake up... it's time for school!")
        self.font = pygame.font.Font(None, 36)
        self.alarmclock_image = pygame.image.load("assets/alarm_clock.png")
        self.alarm_sound = pygame.mixer.Sound("assets/alarm_sound.wav")
        self.history = History()
        self.math_1 = Math()
        self.lunch = Lunch()
        self.end_of_day = End()
        self.state = "WAKEUP"
        self.classes = [self.history, self.math_1, self.lunch, self.end]

    def mainloop(self):
        while self.classes:
            if self.state == "HISTORY":
               self.history()
            elif self.state == "MATH":
                self.math()
            elif self.state == "LUNCH":
                self.lunch()
            if self.state == "END":
                self.end()
            elif self.state == "WAKEUP":
                self.alarm()
        
    def alarm(self):    
        running = True
        alarm_controller = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if alarm_controller:
                self.screen.fill((255, 255, 255))  
                self.screen.blit(self.alarmclock_image, (0, 0))
                text_surface = self.font.render("Hello, Pygame!", True, (0, 0, 0))  
                x = (self.width - text_surface.get_width()) // 2 
                y = (self.height - text_surface.get_height()) // 2
                self.screen.blit(text_surface, (x, y))
                self.alarm_sound.play()
                pygame.display.update()
                alarm_controller = False
                self.state = "HISTORY"
        
    def classloop(self):
         while self.classes:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if self.classes[0] == True:
                self.classes.pop[0]
                pygame.display.update()