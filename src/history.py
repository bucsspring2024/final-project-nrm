import pygame
import requests
import pygame.time


class History():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("History Class")
        self.font = pygame.font.Font(None, 25)
        self.teacher_image = pygame.image.load("assets/History_teacher.png")


        # Initialize self.questions as an empty list
        self.questions = []
        correct_answer = ""
        incorrect_answers = []
        self.first_run= True # Flag to check if it's the first run


        self.current_question_index = 0  # Initialize the current question index
        self.questions = [self.get_trivia_question() for _ in range(2)]
        self.current_question = 0
        self.current_sentence = 0


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


   
    def get_trivia_question(self):
        if not self.questions:  # If there are no more questions
            response= requests.get("https://opentdb.com/api.php?amount=10&category=23&difficulty=medium&type=multiple")
            response.raise_for_status()
            data= response.json()
            self.questions = data['results']
    # Get the first question and remove it from the list
        question_data = self.questions.pop(0)
        return question_data['question'], question_data['correct_answer'], question_data['incorrect_answers']




    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.teacher_image, (0, 0))
   
        # Draw the sentence


        if self.first_run:
            self.screen.blit(self.sentence_surface, self.sentence_rect)
            pygame.display.flip()


        # Wait for 2 seconds
            pygame.time.delay(2000)


        # Clear the screen
            self.screen.fill((255, 255, 255))


        # Set the flag to False after the first run
            self.first_run = False


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
            #    Increment the current question index
            self.current_question_index += 1    


            if self.current_question_index < len(self.questions):
                # Fetch the next question and answers
                question_dict = self.questions[self.current_question_index]
                question = question_dict['question']
                correct_answer = question_dict['correct_answer']
                incorrect_answers = question_dict['incorrect_answers']  


            # Create surfaces with the question and answers and get their rectangles
                self.question_surface = self.font.render(question, True, (0,0,0))
                self.question_rect = self.question_surface.get_rect(center=(400, 300))
                self.correct_answer_surface = self.font.render(correct_answer, True, (0, 0, 0))
                self.correct_answer_rect = self.correct_answer_surface.get_rect(center=(400, 350))
                self.incorrect_answer_surfaces = [self.font.render(answer, True, (0, 0, 0)) for answer in incorrect_answers]
                self.incorrect_answer_rects = [surface.get_rect(center=(400, 400 + i * 50)) for i, surface in enumerate(self.incorrect_answer_surfaces)]
                self.screen.fill((255, 255, 255))
        else:
            # Play laughing sound
            laughing_sound.play()


            # Create a surface with the "Incorrect!" message and get its rectangle
            message_surface = self.font.render("Incorrect!", True, (0, 0, 0))
            message_rect = message_surface.get_rect(center=(300, 500))


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