import pygame

class History():
    '''
    A class representing the history class.

    Attributes:
        screen: A Pygame surface representing the display screen.
        teacher_image: A Pygame image representing the history teacher.
        teacher_sound: A Pygame sound object representing the sound of the history teacher.
    '''

    def __init__(self):
        '''
        Initializes the History object.
        '''
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("History Class")
        self.teacher_image = pygame.image.load("assets/images/history_teacher.png")
        self.teacher_sound = pygame.mixer.Sound("assets/sounds/history_teacher.wav")
