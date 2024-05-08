import pygame
import cv2

class End():
    '''
    A class representing the end of the day scene.

    Attributes:
        font: A Pygame font object for rendering text.
        endofday_image: A Pygame image representing the end of the day scene.
        screen: A Pygame surface representing the display screen.
        text_surface: A Pygame surface containing the first text message.
        text_rect: A Pygame rect representing the position of the first text message.
        text_surface2: A Pygame surface containing the second text message.
        text_rect2: A Pygame rect representing the position of the second text message.
        text_surface3: A Pygame surface containing the third text message.
        text_rect3: A Pygame rect representing the position of the third text message.
        text_surface4: A Pygame surface containing the fourth text message.
        text_rect4: A Pygame rect representing the position of the fourth text message.
        text_surface5: A Pygame surface containing the fifth text message.
        text_rect5: A Pygame rect representing the position of the fifth text message.
        video_capture: An OpenCV video capture object for playing a video.
    '''

    def __init__(self):
        '''
        Initializes the End object.
        '''
        pygame.init()
        self.font = pygame.font.Font(None, 36)
        self.endofday_image = pygame.image.load("assets/images/end_of_day.png")
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("End of the Day")
        self.text_surface = self.font.render("Wow what an interesting day!", True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(400, 100))
        self.text_surface2 = self.font.render("Well it's time to go home lets get on the bus.", True, (0, 0, 0))
        self.text_rect2 = self.text_surface2.get_rect(center=(400, 100))
        self.text_surface3 = self.font.render("Thank you for joining our school.", True, (0, 0, 0))
        self.text_rect3 = self.text_surface3.get_rect(center=(400, 400))
        self.text_surface4 = self.font.render("Have a good evening and hopefully we'll see you tommorrow.", True, (0, 0, 0))
        self.text_rect4 = self.text_surface4.get_rect(center=(400, 450))
        self.text_surface5 = self.font.render("Goodbye!!", True, (0, 0, 0))
        self.text_rect5 = self.text_surface5.get_rect(center=(400, 500))
        self.video_capture = cv2.VideoCapture("assets/images/schoolbus.mp4")

    def draw(self):
        '''
        Draws the end of the day scene.
        '''
        screen = self.screen
        screen.blit(self.endofday_image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(2000)

        screen.fill((255, 255, 255))
        screen.blit(self.endofday_image, (0, 0))  # Redraw the school house image
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.flip()
        pygame.time.delay(3000)  # Wait for 2 seconds

        # Draw the second sentence
        screen.fill((255, 255, 255))  # Fill the screen with white
        screen.blit(self.endofday_image, (0, 0))  # Redraw the school house image
        screen.blit(self.text_surface2, self.text_rect2)
        pygame.display.flip()
        pygame.time.delay(3000)  # Wait for 2 seconds

        # Draw the third sentence
        screen.fill((255, 255, 255))  # Fill the screen with white
        screen.blit(self.endofday_image, (0, 0))  # Redraw the school house image
        screen.blit(self.text_surface3, self.text_rect3)
        screen.blit(self.text_surface4, self.text_rect4)
        screen.blit(self.text_surface5, self.text_rect5)
        pygame.display.flip()
        pygame.time.delay(4000)  # Wait for 2 seconds
      
    def main(self):
        '''
        Main loop for the end of the day scene.
        '''
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw()

            ret, frame = self.video_capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = pygame.surfarray.make_surface(frame)
                self.screen.blit(frame, (0, 0))
                pygame.display.flip()
            else:
                self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

        self.video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    game = End()
    game.main()
