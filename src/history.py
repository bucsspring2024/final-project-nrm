import pygame

class History():
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Hello I am Mr. Adams and this is History 101.")
        self.font = pygame.font.Font(None, 36)
        self.teacher_image = pygame.image.load("History_teacher.png")

        # Create a surface with the text and get its rectangle
        self.text_surface = self.font.render("Hello class, wlcome to History 101." True, (0,0,0))
        self.text_rect = self.text_surface.get_rect(center=(400, 300))
  # Create a surface with the second text and get its rectangle
        self.text_surface2 = self.font.render("Today we are learning about Greek Gods. How many can you name?", True, (0, 0, 0))
        self.text_rect2 = self.text_surface2.get_rect(center=(400, 350))

        self.user_answer= input("Type your answer here:")

        self.text_surface3 = self.font.render("Impressive, thanks for sharing", True, (0, 0, 0))
        self.text_rect3 = self.text_surface3.get_rect(center=(400, 400))

        self.text_surface4 = self.font.render("Oh time to head to your next class. Have fun!!", True, (0, 0, 0))
        self.text_rect4 = self.text_surface4.get_rect(center=(400, 450))

    def draw(self):
        # Draw the first text onto the screen
        self.screen.blit(self.text_surface1, self.text_rect1)

        self.screen.blit(self.text_surface2, self.text_rect2)

        self.screen.blit(self.text_surface3, self.text_rect3)

        self.screen.blit(self.text_surface4, self.text_rect4) 

        pygame.display.flip()
      