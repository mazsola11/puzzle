import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    mouse_position = (0, 0)
    drawing = False
    screen = pygame.display.set_mode((600, 800), 0, 32)
    screen.fill(WHITE)
    pygame.display.set_caption("ScratchBoard")

    pygame.draw.rect(screen, (0, 255, 0), [0, 0, 200, 200])
    x_pos = [x for x in range(200)]
    y_pos = [x for x in range(200)]

    last_pos = None

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                if (drawing):
                    pygame.draw.line(screen, BLACK, last_pos, mouse_position, 3)
                    if mouse_position[0] in x_pos and mouse_position[1] in y_pos:
                        pygame.draw.rect(screen, (255, 0, 0), [0, 0, 200, 200])
                    else:
                        pygame.draw.rect(screen, (0, 255, 0), [0, 0, 200, 200])
                last_pos = mouse_position
            elif event.type == MOUSEBUTTONUP:
                mouse_position = (0, 0)
                drawing = False
            elif event.type == MOUSEBUTTONDOWN:
                drawing = True

        pygame.display.update()

if __name__ == "__main__":
    main()