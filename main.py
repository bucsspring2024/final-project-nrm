import pygame
pygame.init()
screen = pygame.display.set_mode(640,480)
screen.fill("blue")
font = pygame.font.Font(None, 36)
text = font.render("Welcome to the Pizza shop!", True, "white")
text_rect = text.get_rect(640/2,480/2)
screen.blit(text, text_rect)
pygame.display.flip()
pygame.time.wait(3000)


def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

