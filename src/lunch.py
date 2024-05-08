import pygame

class Lunch():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 36)
        self.food_fight_word = pygame.image.load("assets/images/foodfight_logo.png")
        self.cafeteriafood = pygame.image.load("assets/images/cafeteria_food.png")
        self.angryperson = pygame.image.load("assets/images/angryperson.png")
        self.text_surface2 = self.font.render("YOU TOOK MY FOOD!!", True, (0, 0, 0))
        self.text_rect2 = self.text_surface2.get_rect(center=(400, 100))
        self.text_surface3 = self.font.render("I'm gonna start a...", True, (0, 0, 0))
        self.text_rect3 = self.text_surface3.get_rect(center=(400, 100))
        self.second_state_active = False  # Initialize second_state_active attribute
        pygame.display.update()

    def main(self):
        while True:
            self.intro()
            if self.second_state_active:
                self.second_state()  # Call the second_state method

    def intro(self):
        self.screen.blit(self.cafeteriafood, (0, 0))
        pygame.display.set_caption("Lunch Time!")
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.display.set_caption("Click on the screen to take your food!")
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.second_state_active = True  # Set second_state_active to True
        return self.second_state_active

    def second_state(self):
        self.screen.blit(self.angryperson, (0, 0))
        self.screen.blit(self.text_surface2, self.text_rect2)
        pygame.display.flip()
        pygame.time.delay(1000)
        self.food_fight_logo()

    def food_fight_logo(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.food_fight_word, (0, 0))
        pygame.display.flip()
        pygame.time.delay(1000)
        self.foodfight()
        
    def foodfight(self):
        pygame.display.set_caption("Click on the screen to escape the food fight!")
        pictures = ["assets/images/ff1.png", "assets/images/ff2.png", "assets/images/ff3.png"]
        current_picture_index = 0
        while current_picture_index < len(pictures):
            current_picture = pygame.image.load(pictures[current_picture_index]).convert()
            self.screen.blit(current_picture, (0, 0))
            pygame.display.update()
            pygame.time.delay(1000)
            current_picture_index = current_picture_index + 1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.screen.fill((255, 255, 255))  # Correct the fill color

if __name__ == "__main__":
    game = Lunch()
    game.main()



# import pygame

# class Lunch():
#     def __init__(self):
#         pygame.init()
#         pygame.mixer.init()
#         self.screen = pygame.display.set_mode((800, 600))
#         self.font = pygame.font.Font(None, 36)
#         self.food_fight_word = pygame.image.load("assets/images/foodfight_logo.png")
#         self.cafeteriafood = pygame.image.load("assets/images/cafeteria_food.png")
#         self.angryperson = pygame.image.load("assets/images/angryperson.png")
#         self.text_surface2 = self.font.render("YOU TOOK MY FOOD!!", True, (0, 0, 0))
#         self.text_rect2 = self.text_surface2.get_rect(center=(400, 100))
#         self.text_surface3 = self.font.render("I'm gonna start a...", True, (0, 0, 0))
#         self.text_rect3 = self.text_surface3.get_rect(center=(400, 100))
#         pygame.display.update()

#     def main(self):
#         while True:
#             self.intro()
#             if self.secondstate:
#                 self.secondstate()
#             pygame.quit()

#     def intro(self):
#         self.screen.blit(self.cafeteriafood, (0, 0))
#         pygame.display.set_caption("Lunch Time!")
#         pygame.display.update()
#         pygame.time.delay(1000)
#         pygame.display.set_caption("Click on the screen to take your food!")
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 self.secondstate = True
#         return self.secondstate

#     def secondstate(self):
#         self.screen.blit(self.angryperson, (0, 0))
#         self.screen.blit(self.text_surface2, self.text_rect2)
#         pygame.display.flip()
#         pygame.time.delay(1000)
#         self.food_fight_logo()

#     def food_fight_logo(self):
#         self.screen.fill((255, 255, 255))
#         self.screen.blit(self.food_fight_word, (0, 0))
#         pygame.display.flip()
#         pygame.time.delay(1000)
#         self.foodfight()
        
#     def foodfight(self):
#         pygame.display.set_caption("Click on the screen to escape the food fight!")
#         pictures = ["assets/images/ff1.png", "assets/images/ff2.png", "assets/images/ff3.png"]
#         current_picture_index = 0
#         while current_picture_index < len(pictures):
#             current_picture = pygame.image.load(pictures[current_picture_index]).convert()
#             self.screen.blit(current_picture, (0, 0))
#             pygame.display.update()
#             pygame.time.delay(1000)
#             current_picture_index = current_picture_index + 1
#             for event in pygame.event.get():
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     self.screen.fill(255, 255, 255)

# if __name__ == "__main__":
#     game = Lunch()
#     game.main()