import pygame
# import requests
import json
class Math():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Welcome to Math class. I am Mr. Smith and I will be your teacher today.")
        self.font = pygame.font.Font(None, 36)
        self.teacher_image = pygame.image.load("Teacher.png")

        # Fetch a trivia question
        question, correct_answer, incorrect_answers = self.get_trivia_question()

        # Create a surface with the question and get its rectangle
        self.question_surface = self.font.render(question, True, (0,0,0))
        self.question_rect = self.question_surface.get_rect(center=(400, 300))

        # Create surfaces with the answers and get their rectangles
        self.correct_answer_surface = self.font.render(correct_answer, True, (0, 0, 0))
        self.correct_answer_rect = self.correct_answer_surface.get_rect(center=(400, 350))

        self.incorrect_answer_surfaces = [self.font.render(answer, True, (0, 0, 0)) for answer in incorrect_answers]
        self.incorrect_answer_rects = [surface.get_rect(center=(400, 400 + i * 50)) for i, surface in enumerate(self.incorrect_answer_surfaces)]

        self.questions = [self.get_trivia_question() for _ in range(2)]

    def get_trivia_question(self):
        response = requests.get("https://opentdb.com/api.php?amount=2&category=19&difficulty=medium&type=multiple")
        if response.status_code == 200:
            data = json.loads(response.text)
            return data['results'][0]['question'], data['results'][0]['correct_answer'], data['results'][0]['incorrect_answers']
        else:
            print("Failed to get data from trivia API")
            return None

    def draw(self):
        # Draw the question and the answers onto the screen
        self.screen.blit(self.question_surface, self.question_rect)
        self.screen.blit(self.correct_answer_surface, self.correct_answer_rect)
        for surface, rect in zip(self.incorrect_answer_surfaces, self.incorrect_answer_rects):
            self.screen.blit(surface, rect)
        pygame.display.flip()

    def check_answer(self, pos):
        # Check if the clicked position is within the rectangle of the correct answer
            cheering_sound = pygame.mixer.Sound('cheering.wav')
            laughing_sound = pygame.mixer.Sound('laughing.wav')
            if self.correct_answer_rect.collidepoint(pos):
                print("Correct! Great job.")
                cheering_sound.play()
            else:
                print("OOOO better luck next time.")
                laughing_sound.play()

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the position of the mouse when it's clicked
                    pos = pygame.mouse.get_pos()
                    self.check_answer(pos)
            self.draw()
        pygame.quit()

if __name__ == "__main__":
    game = Math()
    game.main()

