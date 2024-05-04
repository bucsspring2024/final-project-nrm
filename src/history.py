import pygame
import requests
import pygame.time
import json

class History():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("History Class")
        self.font = pygame.font.Font(None, 25)
        self.teacher_image = pygame.image.load("assets/History_teacher.png")
        self.questions = []
        correct_answer = ""
        sentence = "Welcome to History class. I am Mrs. Smith and I will be your teacher today. Let's get started"
        self.sentence_surface = self.font.render(sentence, True, (0,0,0))
        self.sentence_rect = self.sentence_surface.get_rect(center=(500, 100))
        
        
        # Fetch a trivia question
        question, correct_answer, incorrect_answers = self.get_trivia_question()
         
        #   Create a surface with the question and get its rectangle
        self.question_surface = self.font.render(question, True, (0,0,0))
        self.question_rect = self.question_surface.get_rect(center=(400, 300))

        # Create surfaces with the answers and get their rectangles
        self.correct_answer_surface = self.font.render(correct_answer, True, (0, 0, 0))
        self.correct_answer_rect = self.correct_answer_surface.get_rect(center=(400, 350))

        self.incorrect_answer_surfaces = [self.font.render(answer, True, (0, 0, 0)) for answer in incorrect_answers]
        self.incorrect_answer_rects = [surface.get_rect(center=(400, 400 + i * 50)) for i, surface in enumerate(self.incorrect_answer_surfaces)]
        self.questions = [self.get_trivia_question() for _ in range(2)]
    
def get_trivia_question(self):
    if not self.questions:  # If there are no more questions
        response = requests.get("https://opentdb.com/api.php?amount=10&category=23&difficulty=medium&type=multiple")
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse the JSON response
        results = data.get('results', [])  # Get the 'results' key from the JSON data, or use an empty list if it doesn't exist
        if results:
            question_data = results[0]  # Get the first question
            return question_data['question'], question_data['correct_answer'], question_data['incorrect_answers']
        else:
            return None, None, [] 
        question_data = self.questions.pop(0)
        return question_data['question'], question_data['correct_answer'], question_data['incorrect_answers']

    def draw(self):
        self.screen.blit(self.teacher_image, (0, 0))

        # Draw the sentence
        self.screen.blit(self.sentence_surface, self.sentence_rect)
        pygame.display.flip()

     # Wait for 2 seconds
        pygame.time.delay(2000)

        # Clear the screen
        self.screen.fill((255, 255, 255))

        # Draw the question and answers
        self.screen.blit(self.teacher_image, (0, 0))
        self.screen.blit(self.question_surface, self.question_rect)
        self.screen.blit(self.correct_answer_surface, self.correct_answer_rect)
        for surface, rect in zip(self.incorrect_answer_surfaces, self.incorrect_answer_rects):
            pygame.draw.rect(self.screen, (255,255,255), rect.inflate(20, 20))
            self.screen.blit(surface, rect)

        pygame.display.flip()


    def check_answer(self, pos):
        cheering_sound = pygame.mixer.Sound('assets/cheering.wav')
        laughing_sound = pygame.mixer.Sound("assets/laughing.wav")

        # Check if the correct answer was clicked
        if self.correct_answer_rect.collidepoint(pos):
            # Play cheering sound
            cheering_sound.play()

            # Create a surface with the "Correct!" message and get its rectangle
            message_surface = self.font.render("Correct!", True, (0, 0, 0))
            message_rect = message_surface.get_rect(center=(400, 500))
        else:
            # Play laughing sound
            laughing_sound.play()

            # Create a surface with the "Incorrect!" message and get its rectangle
            message_surface = self.font.render("Incorrect!", True, (0, 0, 0))
            message_rect = message_surface.get_rect(center=(350, 500))

        # Draw a white rectangle behind the message
        pygame.draw.rect(self.screen, (255, 255, 255), message_rect.inflate(20, 20))

        # Draw the message
        self.screen.blit(message_surface, message_rect)

        pygame.display.flip()

        # Wait for 2 seconds before clearing the message
        pygame.time.delay(2000)

        # Clear the screen
        self.screen.fill((255, 255, 255))
        pygame.display.flip()

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.check_answer(pos)
            self.draw()
            self.classover = False

        pygame.quit()

if __name__ == "__main__":
    game = History()
    game.main()