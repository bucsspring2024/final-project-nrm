import pygame

class Math():
    '''
    A class representing the math class.

    Attributes:
        screen: A Pygame surface representing the display screen.
        teacher_image: A Pygame image representing the math teacher.
        teacher_sound: A Pygame sound object representing the sound of the math teacher.
    '''

    def __init__(self):
        '''
        Initializes the Math object.
        '''
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Math Class")
        self.teacher_image = pygame.image.load("assets/images/math_teacher.png")
        self.teacher_sound = pygame.mixer.Sound("assets/sounds/math_teacher.wav")
