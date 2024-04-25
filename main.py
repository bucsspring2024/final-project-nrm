import pygame
pygame.init()
screen = pygame.display.set_mode()
width, height = pygame.display.get_window_size()
screen.fill("blue")
def main():
     pygame.init()
     controller = Controller()
     controller.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()


user class
hairstyle class

