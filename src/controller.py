import pygame

from src.academics import Academics
from src.lunch import Lunch
from src.end_of_day import End

class Controller:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.alarm_image = pygame.image.load("assets/images/alarm_clock.png")
        self.alarm_sound = pygame.mixer.Sound("assets/sounds/alarm_sound.wav")
        self.lunch = Lunch()
        self.end = End()
        self.academics = Academics()
        self.alarm = True
        self.classes = False
        
    def mainloop(self):
        running = True
        while running and self.classes:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if self.alarm and self.classes == False:
                self.alarmfunc()
            elif self.classes and self.alarm == False:
                class_instance = self.classes[0]
                class_instance.main()
                pygame.display.update()
                self.classes.pop(0)
    
    def alarmfunc(self):
        self.screen.blit(self.alarm_image, (0, 0))
        self.alarm_sound.play()
        pygame.time.delay(1000)
        pygame.display.update()
        pygame.display.set_caption("Click the screen to start your day!")
        pygame.display.update()
        self.classes = [self.end, self.lunch, self.academics]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and self.alarm:
                self.alarm_sound.stop()
                self.alarm = False
                return self.alarm and self.classes