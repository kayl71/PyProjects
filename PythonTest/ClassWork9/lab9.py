import pygame

WIDTH, HEIGHT = 500, 500
FPS_MAX = 30

pygame.init()

screen = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock()


# rect(screen, (255, 0, 255), (100, 100, 200, 200))
# rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
# polygon(screen, (255, 255, 0), [(100,100), (200,50),
#                                (300,100), (100,100)])
# polygon(screen, (0, 0, 255), [(100,100), (200,50),
#                                (300,100), (100,100)], 5)
# circle(screen, (0, 255, 0), (200, 175), 50)
# circle(screen, (255, 255, 255), (200, 175), 50, 5)
#
def SumPos(pos1, pos2):
    return pos1[0] - pos2[0], pos1[1] - pos2[1]

screen.fill((200, 200, 200))

pos = (HEIGHT / 2, WIDTH / 2)

screen.fill((200, 200, 200))
pygame.draw.circle(screen, (255, 255, 0), pos, 100, 0)
pygame.draw.circle(screen, (0, 0, 0), pos, 100, 1)

pygame.draw.circle(screen, (255, 0, 0), SumPos(pos, (35, 10)), 18, 0)
pygame.draw.circle(screen, (0, 0, 0), SumPos(pos, (35, 10)), 18, 1)
pygame.draw.circle(screen, (0, 0, 0), SumPos(pos, (35, 10)), 10, 0)
pygame.draw.circle(screen, (255, 0, 0), SumPos(pos, (-35, 10)), 13, 0)
pygame.draw.circle(screen, (0, 0, 0), SumPos(pos, (-35, 10)), 13, 1)
pygame.draw.circle(screen, (0, 0, 0), SumPos(pos, (-35, 10)), 8, 0)

pygame.draw.polygon(screen, (0, 0, 0), [
    SumPos(pos, (50, 50)),
    SumPos(pos, (60, 60)),
    SumPos(pos, (30, 30)),
    SumPos(pos, (20, 20))], 5)
pygame.draw.polygon(screen, (0, 0, 0), [
    SumPos(pos, (-50, 50)),
    SumPos(pos, (-60, 60)),
    SumPos(pos, (-25, 20)),
    SumPos(pos, (-15, 10))], 5)
pygame.draw.rect(screen, (0, 0, 0), (pos[0] + -45, pos[1] + 50, 90, 20))

pygame.display.update()

while True:
    clock.tick(FPS_MAX)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
