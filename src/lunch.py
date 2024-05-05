import pygame
class Lunch():
    def __init__(self):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load("assets/talking.wav")
        pygame.mixer.music.play(-1)
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Lunch_time")
        self.font = pygame.font.Font(None, 36)
        self.Lunch_image = pygame.image.load("assets/lunch_room.webp")
        self.food_fight = pygame.image.load("assets/FoodFight.png")
        self.food_fight_word= pygame.image.load("assets/foodfight_logo.png")

        self.text_surface1 = self.font.render("It time for lunch. Lets go sit down and", True, (0, 0, 0))
        self.text_rect1 = self.text_surface1.get_rect(center=(400, 100))
        self.text_surface2= self.font.render("eat some food with your friends.", True, (0, 0, 0))
        self.text_rect2 = self.text_surface2.get_rect(center=(400, 150))
    
        self.text_surface3 = self.font.render("Oo,is that a sandwhich?", True, (0, 0, 0))
        self.text_rect3 = self.text_surface3.get_rect(center=(400, 100))

        self.text_surface4 = self.font.render("It looks delicious", True, (0, 0, 0))
        self.text_rect4 = self.text_surface4.get_rect(center=(400, 100))

        self.text_surface5 = self.font.render("Oh no, that table started a... ", True, (0, 0, 0))
        self.text_rect5 = self.text_surface5.get_rect(center=(400, 100))

        self.text_surface6 = self.font.render("We better get out of here.", True, (0, 0, 0))
        self.text_rect6 = self.text_surface6.get_rect(center=(400, 100))

        self.cafe_chatter = pygame.mixer.Sound("assets/lunch_chatting.mp3")
        self.fighting_sound = pygame.mixer.Sound("assets/fighting.mp3")   
        
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.Lunch_image, (0, 0))
        self.screen.blit(self.text_surface1, self.text_rect1)
        self.screen.blit(self.text_surface2, self.text_rect2)
        self.cafe_chatter.play()
        pygame.display.flip()
        pygame.time.delay(4000)

        self.screen.fill((255, 255, 255))   
        self.screen.blit(self.Lunch_image, (0, 0))
        self.screen.blit(self.text_surface3, self.text_rect3)
        pygame.display.flip()
        pygame.time.delay(4000)

        
        self.screen.fill((255, 255, 255))   
        self.screen.blit(self.Lunch_image, (0, 0))
        self.screen.blit(self.text_surface4, self.text_rect4)
        pygame.display.flip()
        pygame.time.delay(4000)

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.Lunch_image, (0, 0))
        self.screen.blit(self.text_surface5, self.text_rect5)
        self.cafe_chatter.stop()
        pygame.display.flip()
        pygame.time.delay(4000)

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.food_fight_word, (0, 0))
        self.fighting_sound.play()
        pygame.display.flip()
        pygame.time.delay(4000)

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.food_fight, (0, 0))
        pygame.display.flip()
        pygame.time.delay(4000)

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.food_fight, (0, 0))
        self.screen.blit(self.text_surface6, self.text_rect6)
        self.fighting_sound.play() 
        pygame.display.flip()
        pygame.time.delay(4000)
        

    def main(self):
       running = True
       while running:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   running = False
           self.draw()
           self.classover = False
       pygame.quit()


if __name__ == "__main__":
    game = Lunch()
    game.main()