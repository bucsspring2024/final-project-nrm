# questions:
# plan for structure: use self.state to transition between different classes
# how to incoporate a teacher in each class - transparent png over background?
# how to get people to answer questions - prompted by screen, then input their answer, etc




import pygame

from src.history import History
from src.math import Math
from src.lunch import Lunch
from src.end_of_day import EndDay

class Controller():
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Wake up... it's time for school!")
        self.font = pygame.font.Font(None, 36)
        self.alarmclock_image = pygame.image.load("alarmclock.png")
        self.alarm_sound = pygame.mixer.Sound("alarm_sound.wav")
        self.history = History()
        self.math = Math()
        self.lunch = Lunch()
        self.end = EndDay()
        self.state = "WAKEUP"
        self.classes = [self.history, self.math, self.lunch, self.end]

    def mainloop(self):
        while self.classes:
            if self.state == "HISTORY":
               self.historyclass()
            elif self.state == "MATH":
                self.mathclass()
            elif self.state == "LUNCH":
                self.lunchclass()
            if self.state == "END":
                self.endofday()
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
            if self.classes[0].classover == True:
                self.classes.pop[0]
                pygame.display.update()

if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()