import pygame
import requests
import pygame.time

class Math():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Math Class")
        self.font = pygame.font.Font(None, 25)
        self.teacher_image = pygame.image.load("assets/Math_teacher.png")
        self.questions = []
        correct_answer = ""
        sentence = "Hello, I am Mrs. Woodrow and this math class, we are going to have some fun. Let's get started."
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
            response = requests.get("https://opentdb.com/api.php?amount=2&category=19&difficulty=medium&type=multiple")
            data = response.json()  # Parse the JSON response
            self.questions = data['results']  # Store the questions

    # Get the first question and remove it from the list
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

            # Rest of the code...


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
   game = Math()
   game.main()
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((800, 600))
#         pygame.display.set_caption("Welcome to Math class. I am Mr. Smith and I will be your teacher today.")
#         self.font = pygame.font.Font(None, 36)
#         self.teacher_image = pygame.image.load("assets/Teacher.png")

#         question, correct_answer, incorrect_answers = self.get_trivia_question()

#         self.question_surface = self.font.render(question, True, (0,0,0))
#         self.question_rect = self.question_surface.get_rect(center=(400, 300))

#         self.correct_answer_surface = self.font.render(correct_answer, True, (0, 0, 0))
#         self.correct_answer_rect = self.correct_answer_surface.get_rect(center=(400, 350))

#         self.incorrect_answer_surfaces = [self.font.render(answer, True, (0, 0, 0)) for answer in incorrect_answers]
#         self.incorrect_answer_rects = [surface.get_rect(center=(400, 400 + i * 50)) for i, surface in enumerate(self.incorrect_answer_surfaces)]

#         self.questions = [self.get_trivia_question() for _ in range(2)]

#     def get_trivia_question(self):
#         response = requests.get("https://opentdb.com/api.php?amount=2&category=19&difficulty=medium&type=multiple")
#         if response.status_code == 200:
#             data = json.loads(response.text)
#             return data['results'][0]['question'], data['results'][0]['correct_answer'], data['results'][0]['incorrect_answers']
#         else:
#             print("Failed to get data from trivia API")
#             return None

#     def draw(self):
#         self.screen.blit(self.question_surface, self.question_rect)
#         self.screen.blit(self.correct_answer_surface, self.correct_answer_rect)
#         for surface, rect in zip(self.incorrect_answer_surfaces, self.incorrect_answer_rects):
#             self.screen.blit(surface, rect)
#         pygame.display.flip()

#     def check_answer(self, pos):
#             cheering_sound = pygame.mixer.Sound("assets/cheering.wav")
#             laughing_sound = pygame.mixer.Sound("assets/laughing.wav")
#             if self.correct_answer_rect.collidepoint(pos):
#                 print("Correct! Great job.")
#                 cheering_sound.play()
#             else:
#                 print("Oh man... better luck next time.")
#                 laughing_sound.play()

#     def main(self):
#         running = True
#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                 elif event.type == pygame.MOUSEBUTTONDOWN:
#                     pos = pygame.mouse.get_pos()
#                     self.check_answer(pos)
#             self.draw()
#         pygame.quit()

# if __name__ == "__main__":
#     game = Math()
#     game.main()

