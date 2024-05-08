import pygame

class History():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("History Class")
        self.teacher_image = pygame.image.load("assets/images/history_teacher.png")
        # self.teacher_sound = pygame.mixer.Sound("assets/sounds/history_teacher.wav")
        #add teacher sound