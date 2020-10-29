import pygame, sys
import os
from pygame.locals import *

def main():
    pygame.init()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)

    START_POINT = (25, 25)
    LINE_LENGTH = 200

    vertices = [[1, 1],
                [1, 1],
                [0, 1]]
    vertices[0][0] = 2



    cursor_img = pygame.transform.scale(pygame.image.load(os.path.join('images', 'cursor.png')), (50, 50))
    cursor_x = 0
    cursor_y = 0

    screen = pygame.display.set_mode((600, 600), 0, 32)
    pygame.display.set_caption("Puzzle solver")

    # pygame.draw.circle(screen, WHITE, (50, 300), 30)
    # pygame.draw.circle(screen, WHITE, (550, 300), 13)

    surface = pygame.Surface((600, 600))
    surface.fill(BLUE)

    for i in range(len(vertices)):
        for j in range(len(vertices[0])):
            if vertices[i][j] in [1, 2]:
                if i+1 < len(vertices) and vertices[i+1][j] in [1, 2]:
                    pygame.draw.rect(surface, WHITE, [START_POINT[0] + j * LINE_LENGTH,
                                                      START_POINT[1] + i * LINE_LENGTH,
                                                      20,
                                                      LINE_LENGTH])

                if j+1 < len(vertices[0]) and vertices[i][j+1] in [1, 2]:
                    pygame.draw.rect(surface, WHITE, [START_POINT[0] + j * LINE_LENGTH,
                                                      START_POINT[1] + i * LINE_LENGTH,
                                                      LINE_LENGTH,
                                                      20])


    while True:
        screen.blit(surface, (0, 0))
        prev = (cursor_x, cursor_y)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cursor_x = max(cursor_x-1, 0)
                if event.key == pygame.K_RIGHT:
                    cursor_x = min(cursor_x+1, len(vertices[0])-1)
                if event.key == pygame.K_UP:
                    cursor_y = max(cursor_y-1, 0)
                if event.key == pygame.K_DOWN:
                    cursor_y = min(cursor_y+1, len(vertices)-1)


        if vertices[cursor_y][cursor_x] == 1:
            vertices[cursor_y][cursor_x] = 2
            vertices[prev[1]][prev[0]] = 1

        else:
            cursor_x, cursor_y = prev

        screen.blit(cursor_img, (START_POINT[0] + cursor_x*LINE_LENGTH,
                                 START_POINT[1] + cursor_y*LINE_LENGTH))
        pygame.display.update()

if __name__ == "__main__":
    main()