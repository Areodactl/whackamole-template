import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        width = 640
        height = 512
        screen = pygame.display.set_mode((width, height))
        clock = pygame.time.Clock()
        running = True
        mole_x, mole_y = 0, 0
        color = (0, 0, 0)

        while running:
            screen.fill("light green")
            for x in range(0, width, 32):
                pygame.draw.line(screen, color, (x,0), (x,height))
            for y in range(0, height, 32):
                pygame.draw.line(screen, color, (0, y), (width, y))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mole_loc = mole_image.get_rect(topleft=(mole_x,mole_y))
                    if mole_loc.collidepoint(event.pos):
                        mole_x = random.randrange(0, width // 32) * 32
                        mole_y = random.randrange(0, height // 32) * 32
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
