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
        self.Lunch_image = pygame.image.load("assets/Lunchroom.png")

        self.caf_chatter = pygame.mixer.Sound("assets/lunch_chatting.mp3")

        self.text_surface1 = self.font.render("It time for lunch. Lets go sit down and eat some food with your friends", True, (0, 0, 0))
        self.text_rect1 = self.text_surface1.get_rect(center=(400, 300))
       

        # person asking player
        self.text_surface2 = self.font.render("What are you having for lunch", True, (0, 0, 0))
        self.text_rect2 = self.text_surface2.get_rect(center=(400, 350))

        self.text_surface3 = self.font.render("Yum, that sounds delicious.", True, (0, 0, 0))
        self.text_rect3 = self.text_surface3.get_rect(center=(400, 400))

        self.text_surface4 = self.font.render("Oh no, that table started a... ", True, (0, 0, 0))
        self.text_rect4 = self.text_surface4.get_rect(center=(400, 450))
        pygame.mixer.music.load('assets/fighting.mp3')
        pygame.mixer.music.play()  # The -1 makes the sound loop indefinitely

        
        self.image = pygame.image.load("assets/FoodFight.png")
        self.image_rect = self.image.get_rect(center=(400, 300))

        self.text_surface5 = self.font.render("We better get out of here.", True, (0, 0, 0))
        self.text_rect5 = self.text_surface5.get_rect(center=(400, 500))
    def play_people_talking(self):
        caf_chatter = pygame.mixer.Sound("assets/lunch_chatting.mp3")
        fighting_sound = pygame.mixer.Sound("assets/fighting.mp3")   
        
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.Lunch_image, (0, 0))
        self.screen.blit(self.text_surface1, self.text_rect1)
        pygame.display.flip()
        pygame.time.delay(2000)

        self.screen.fill((255, 255, 255))   
        self.screen.blit(self.Lunch_image, (0, 0))
        self.screen.blit(self.text_surface2, self.text_rect2)
        pygame.display.flip()
        pygame.time.delay(2000)
        
        self.screen.fill((255, 255, 255))   
        self.screen.blit(self.Lunch_image, (0, 0))
        self.screen.blit(self.text_surface3, self.text_rect3)
        pygame.display.flip()
        pygame.time.delay(2000)

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.Lunch_image, (0, 0))
        self.screen.blit(self.text_surface4, self.text_rect4)
        pygame.display.flip()
        pygame.time.delay(2000)

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.Lunch_image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(2000)

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.Lunch_image, (0, 0))
        self.screen.blit(self.image, self.image_rect)
        pygame.display.flip()
        pygame.time.delay(2000)

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.Lunch_image, (0, 0))
        self.screen.blit(self.text_surface5, self.text_rect5)
        pygame.display.flip()
        pygame.time.delay(2000)

        

if __name__ == "__main__":
    game = Lunch()
    game.main()