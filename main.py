import pygame

from world import World
from agent import Agent

from minds import PassiveMind


if __name__ == '__main__':
    # setup world and add an agent
    world = World(800, 600)
    mind = PassiveMind()
    agent = Agent(mind)
    world.add(agent)

    pygame.init()
    pygame.display.set_caption('Playground')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((world.width, world.height), pygame.HWSURFACE, 32)
    world.render(screen)
    pygame.display.update()

    running = True

    while running:
        clock.tick(60)
        world.update()
        world.render(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
