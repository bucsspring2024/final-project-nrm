import pygame
class EndDay():
   def __init__ (self, ):
      self.font = pygame.font.Font(None, 36)
      self.endofday_image = pygame.image.load("school_house.png")
      pygame.display.set_caption("End of the Day")
      self.text_surface = self.font.render("Wow what an interesting day!", True, (0, 0, 0))
      self.text_rect = self.text_surface.get_rect(center=(400, 300))
      self.text_surface2 = self.font.render("It's time for you to get on the bus to go home.", True, (0, 0, 0))
      self.text_rect2 = self.text_surface2.get_rect(center=(400, 350))
      # click on bus image to go home?
      self.text_surface3 = self.font.render("Thank you for joining our school.Have a good evening and hopefully we'll see you tommorrow.", True, (0, 0, 0))
      self.text_rect3 = self.text_surface3.get_rect(center=(400, 400))
      self.car_sound = pygame.mixer.Sound('car_noise.wav')

   def play_car_noise(self):
        # Play the car noise
        self.car_sound.play()

   def draw(self, screen):
      # Draw the end of the day screen
      screen.fill((255, 255, 255))
      screen.blit(self.endofday_image, (0, 0))
      screen.blit(self.text_surface, self.text_rect)
      screen.blit(self.text_surface2, self.text_rect2)
      screen.blit(self.text_surface3, self.text_rect3)
      pygame.display.flip()


   def main(self):
      running = True
      while running:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False
         self.draw()
      pygame.quit()

if __name__ == "__main__":
      game = EndDay()
      game.main()