import pygame
import requests
import pygame.time
from src.history_class import History
from src.math_class import Math

class Academics():
    def __init__(self):
        pygame.init()
        self.history = History()
        self.math = Math()
        self.academic_classes = [self.history, self.math]
        self.screen = pygame.display.set_mode((800, 600))
        self.cheering_sound = pygame.mixer.Sound('assets/cheering.wav')
        self.questions = []
        self.question_text = ""
        self.correct_answer = ""
        self.incorrect_answers = []
        self.answer_texts = []
        self.question_surface = None
        self.question_rect = None
        self.answer_surfaces = []
        self.answer_rects = []
        self.question_counter = 0
    
    def classroom_view(self):
        for class_instance in self.academic_classes:
            class_instance.trivia()
    
    def trivia():
        
    
    
    
            