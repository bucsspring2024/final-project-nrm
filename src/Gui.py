import pygame
import pygame_menu
pygame.init()
screen = pygame.display.set_mode((800, 600))
def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu('Welcome to School Simulator', 600, 500,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Enter Name Here:', default='')
menu.add.text_input('Click below to begin')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
