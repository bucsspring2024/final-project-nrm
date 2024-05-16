import pygame
from src.controller import Controller

def main():
    '''
    Main function to start the school simulator.

    It initializes Pygame, creates a Controller instance, and starts the main loop of the controller.
    '''
    pygame.init()
    controller = Controller()
    controller.mainloop()
    
if __name__ == '__main__':
    main()
