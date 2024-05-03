import pygame
class Lunch():
    def __init__(self):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load("assets/talking.wav")
        pygame.mixer.music.play(-1)
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption()
        self.font = pygame.font.Font(None, 36)
        self.teacher_image = pygame.image.load("Lunchroom.png")

        self.text_surface1 = self.font.render("It time for lunch. Lets go sit down and eat some food with your friends", True, (0, 0, 0))
        self.text_rect1 = self.text_surface1.get_rect(center=(400, 300))
       

        # person asking player
        self.text_surface2 = self.font.render("What are you having for lunch", True, (0, 0, 0))
        self.text_rect2 = self.text_surface2.get_rect(center=(400, 350))

        self.user_answer= input("Type your answer here:")

        self.text_surface3 = self.font.render("Yum, that sounds delicious.", True, (0, 0, 0))
        self.text_rect3 = self.text_surface3.get_rect(center=(400, 400))

        self.text_surface4 = self.font.render("Oh no, that table started a... FOOD FIGHT!!!", True, (0, 0, 0))
        self.text_rect4 = self.text_surface4.get_rect(center=(400, 450))
        pygame.mixer.music.load('fighting_sounds.mp3')
        pygame.mixer.music.play()  # The -1 makes the sound loop indefinitely

        
        self.image = pygame.image.load("FoodFight.png")
        self.image_rect = self.image.get_rect(center=(400, 300))
        self.fighting_sound = pygame.mixer.Sound('fighting_sound.wav')

        self.text_surface5 = self.font.render("We better get out of here.", True, (0, 0, 0))
        self.text_rect5 = self.text_surface5.get_rect(center=(400, 500))
    def play_people_talking(self):
        # Play the people talking sound
        self.people_talking_sound.play()
    def play_fighting_sound(self):
        # Play the fighting sound
        self.fighting_sound.play()
    def draw(self):
        self.screen.blit(self.text_surface1, self.text_rect1)

        self.screen.blit(self.text_surface2, self.text_rect2)

        self.screen.blit(self.text_surface3, self.text_rect3)

        self.screen.blit(self.text_surface4, self.text_rect4)

        self.screen.blit(self.image, self.image_rect)

        self.screen.blit(self.text_surface5, self.text_rect5)

        pygame.display.flip()

if __name__ == "__main__":
    game = Lunch()
    game.main()