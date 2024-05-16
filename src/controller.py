import pygame

from src.academics import Academics
from src.lunch import Lunch
from src.end_of_day import End


class Controller:
    '''
    A class representing the controller for managing the daily routine.

    Attributes:
        width: An integer representing the width of the display screen.
        height: An integer representing the height of the display screen.
        screen: A Pygame surface representing the display screen.
        alarm_image: A Pygame image representing the alarm clock.
        alarm_sound: A Pygame sound object representing the alarm sound.
        lunch: An instance of the Lunch class for managing lunchtime activities.
        end: An instance of the End class for managing end-of-day activities.
        academics: An instance of the Academics class for managing academic activities.
        alarm: A boolean indicating whether the alarm is active.
        classes: A list containing instances of classes representing daily activities.
    '''

    def __init__(self):
        '''
        Initializes the Controller object.
        '''
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
        self.classes = []

    def mainloop(self):
        '''
         Main loop for controlling the daily routine.
        '''
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if self.alarm and not self.classes:
                self.alarmfunc()
            elif self.classes and not self.alarm:
                class_instance = self.classes[0]
                class_instance.main()
                pygame.display.update()
                self.classes.pop(0)
            running = False

    def alarmfunc(self):
        '''
         Manages the alarm functionality.
        '''
        self.screen.blit(self.alarm_image, (0, 0))
        self.alarm_sound.play()
        pygame.time.delay(1000)
        pygame.display.set_caption("Click the screen to start your day!")
        pygame.display.update()
        self.classes = [self.academics, self.lunch, self.end]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and self.alarm:
                self.alarm_sound.stop()
                self.alarm = False



# class Controller:
#     def __init__(self):
#         pygame.init()
#         self.width = 800
#         self.height = 600
#         self.screen = pygame.display.set_mode((self.width, self.height))
#         self.alarm_image = pygame.image.load("assets/images/alarm_clock.png")
#         self.alarm_sound = pygame.mixer.Sound("assets/sounds/alarm_sound.wav")
#         self.lunch = Lunch()
#         self.end = End()
#         self.academics = Academics()
#         self.alarm = True
#         self.classes = False
        
#     def mainloop(self):
#         running = True
#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#             if self.alarm and self.classes == False:
#                 self.alarmfunc()
#             elif self.classes and self.alarm == False:
#                 class_instance = self.classes[0]
#                 class_instance.main()
#                 pygame.display.update()
#                 self.classes.pop[0]
#         running = False
    
#     def alarmfunc(self):
#         self.screen.blit(self.alarm_image, (0, 0))
#         self.alarm_sound.play()
#         pygame.time.delay(1000)
#         pygame.display.set_caption("Click the screen to start your day!")
#         pygame.display.update()
#         self.classes = [self.academics, self.lunch, self.end]
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONDOWN and self.alarm:
#                 self.alarm_sound.stop()
#                 self.alarm = False
#             return self.alarm and self.classes