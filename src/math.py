import pygame

class Math_class():
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption()
        self.font = pygame.font.Font(None, 36)
        self.teacher_image = pygame.image.load("Teacher.png")

        self.text_surface1 = self.font.render("Welcome to Math class. I am Mr. Smith and I will be your teacher today.", True, (0, 0, 0))
        self.text_rect1 = self.text_surface1.get_rect(center=(400, 300))

        self.text_surface2 = self.font.render("Today we are learning advaced multiplication. What is 24 multiplied by 20 ?", True, (0, 0, 0))
        self.text_rect2 = self.text_surface2.get_rect(center=(400, 350))

        self.user_answer= input("Type your answer here:")

        if self.user_answer == "480":
            self.text_surface3 = self.font.render("Correct! Well done.", True, (0, 0, 0))
        else:
            self.text_surface3 = self.font.render("So Close. The correct answer is 480.", True, (0, 0, 0))
        self.text_rect3 = self.text_surface3.get_rect(center=(400, 400))
    
        self.text_surface4 = self.font.render("Thanl you for joining me, have a good day rest of your day.", True, (0, 0, 0))

    def draw(self):
        self.screen.blit(self.text_surface1, self.text_rect1)

        self.screen.blit(self.text_surface2, self.text_rect2)

        self.screen.blit(self.text_surface3, self.text_rect3)

        pygame.display.flip()