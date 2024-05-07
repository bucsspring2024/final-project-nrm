import pygame
# import sys

class Lunch():
    def __init__(self):
        pygame.mixer.init()
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Lunch Time!")
        self.font = pygame.font.Font(None, 36)
        self.food_fight_word = pygame.image.load("assets/images/foodfight_logo.png")
        self.cafeteriafood = pygame.image.load("assets/images/cafeteria_food.png")
        self.text_surface1 = self.font.render("It's time for lunch. Click the screen to get your food", True, (0, 0, 0))
        self.text_rect1 = self.text_surface1.get_rect(center=(400, 100))
        self.angryperson = pygame.image.load("assets/images/angryperson.png")
        self.text_surface2 = self.font.render("YOU TOOK MY FOOD!!", True, (0, 0, 0))
        self.text_rect2 = self.text_surface2.get_rect(center=(400, 100))
        self.text_surface3 = self.font.render("I'm gonna start a...", True, (0, 0, 0))
        self.text_rect3 = self.text_surface3.get_rect(center=(400, 100))
        self.state = "FIRST"

    def main(self):
        running = True
        while running:
            if self.state == "FIRST":
                self.intro()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
        pygame.quit()

    def intro(self):
        self.screen.blit(self.cafeteriafood, (0, 0))
        self.screen.blit(self.text_surface1, self.text_rect1)
        pygame.display.flip()
        pygame.time.delay(4000)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.nextstate()
        self.classover = False

    def nextstate(self):
        self.screen.blit(self.angryperson, (0, 0))
        self.screen.blit(self.text_surface2, self.text_rect2)
        pygame.display.flip()
        pygame.time.delay(4000)
        self.food_fight_logo()

    def food_fight_logo(self):
        self.screen.blit(self.food_fight_word, (0, 0))
        pygame.display.flip()
        pygame.time.delay(4000)
        self.foodfight()
        
    def foodfight(self):
        pygame.display.set_caption("Click on the screen to escape the food fight!")
        pictures = ["assets/ff1.png", "assets/ff2.png", "assets/ff3.png"]  # Fixed typo in the list
        current_picture_index = 0
        while current_picture_index < len(pictures):  # Loop through pictures
            current_picture = pygame.image.load(pictures[current_picture_index]).convert()
            self.screen.blit(current_picture, (0, 0))  # Blit current picture onto the screen
            pygame.display.update()  # Update the display
            pygame.time.delay(1000)  # 1000 milliseconds = 1 second
            current_picture_index += 1  # Move to the next picture
            for event in pygame.event.get():  # Check for events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = "END"
                    self.classover = False
                    return  # Exit the method if clicked

if __name__ == "__main__":
    game = Lunch()
    game.main()