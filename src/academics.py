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
    
    def screen_display(self):
        for class_instance in self.academic_classes():
            self.screen.blit(class_instance.teacher_image, (0, 0))
            self.class_instance.teacher_sound.play()
            pygame.time.wait(int(self.teacher_sound.get_length() * 1000))
    
    def get_trivia_question(self):
        response = requests.get("https://opentdb.com/api.php?amount=1&category=23&difficulty=medium&type=multiple")
        data = response.json()  # Parse the JSON response
        if data['response_code'] == 0:
            question_data = data['results'][0]
            self.question_text = question_data['question']
            self.correct_answer = question_data['correct_answer']
            self.incorrect_answers = question_data['incorrect_answers']
            self.answer_texts = self.incorrect_answers + [self.correct_answer]  # Store all answer texts

                # Create surfaces and rectangles for question and answers
            self.question_surface = self.font.render(self.question_text, True, (0, 0, 0))
            self.question_rect = self.question_surface.get_rect(center=(400, 200))
            self.answer_surfaces = [self.font.render(answer, True, (0, 0, 0)) for answer in self.answer_texts]
            self.answer_rects = [surface.get_rect(center=(400, 300 + i * 50)) for i, surface in enumerate(self.answer_surfaces)]

    def draw_trivia_questions(self):
        if self.question_surface is not None:
            self.screen.blit(self.question_surface, self.question_rect)
            for surface, rect in zip(self.answer_surfaces, self.answer_rects):
                pygame.draw.rect(self.screen, (200, 200, 200), rect)  # Draw background for answers
                self.screen.blit(surface, rect)
        pygame.display.flip()
        
    def check_answer(self, pos):
        for answer_text, rect in zip(self.answer_texts, self.answer_rects):
            if rect.collidepoint(pos):
                if answer_text == self.correct_answer:
                    self.show_feedback(True)  # Show feedback for correct answer
                    self.cheering_sound.play()
                else:
                    self.show_feedback(False)  # Show feedback for incorrect answer
                # Clear question and answer surfaces
                self.question_surface = None
                self.answer_surfaces = []
                break  # Exit the loop after selecting an answer

    def show_feedback(self, is_correct):
        message = "Correct!" if is_correct else "Incorrect!"
        feedback_surface = self.big_font.render(message, True, (0, 255, 0) if is_correct else (255, 0, 0))
        feedback_rect = feedback_surface.get_rect(center=(400, 300))
        self.screen.blit(feedback_surface, feedback_rect)

    def main(self):
        while self.question_counter <= 4:
            self.screen_display()  # Draw the current state
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.check_answer(pos)  # Check if the user clicked on an answer
                    self.get_trivia_question()  # Get the next trivia question after user input
                    self.question_counter = self.question_counter + 1
            pygame.display.flip()  # Update the display
        
        pygame.quit()

if __name__ == "__main__":
    game = Academics()
    game.main()