import pygame
import requests
import pygame.time

class History():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("History Class")
        self.font = pygame.font.Font(None, 25)
        self.big_font = pygame.font.Font(None, 50)
        self.teacher_image = pygame.image.load("assets/History_teacher.png")
        self.questions = []
        self.question_text = ""
        self.correct_answer = ""
        self.incorrect_answers = []
        self.answer_texts = []  # Store answer texts separately
        self.question_surface = None
        self.question_rect = None
        self.answer_surfaces = []
        self.answer_rects = []

        self.get_trivia_question()

        self.classover = False

    def get_trivia_question(self):
        if not self.questions:  # If there are no more questions
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
                self.answer_rects = [surface.get_rect(center=(400, 300 + i * 50)) for i, surface in
                                      enumerate(self.answer_surfaces)]

    def draw(self):
        self.screen.fill((255, 255, 255))  # Clear the screen
        self.screen.blit(self.teacher_image, (0, 0))  # Draw teacher image

        # Draw the question and answers if they exist
        if self.question_surface is not None:
            self.screen.blit(self.question_surface, self.question_rect)
            for surface, rect in zip(self.answer_surfaces, self.answer_rects):
                pygame.draw.rect(self.screen, (200, 200, 200), rect)  # Draw background for answers
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