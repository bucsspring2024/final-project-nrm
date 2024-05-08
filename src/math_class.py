import pygame

class Math():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Math Class")
        self.teacher_image = pygame.image.load("assets/images/math_teacher.png")
        self.teacher_sound = pygame.mixer.Sound("assets/sounds/math_teacher.wav")