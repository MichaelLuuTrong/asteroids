import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids in a {SCREEN_WIDTH}x{SCREEN_HEIGHT} window...")
    pygame.init()
    pygame.font.init()

    score_font = pygame.font.SysFont('dejavuserif', 20)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    dt = 0
    score = 0
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()
    player_ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        scoreboard = score_font.render(f"Score: {int(score)}", False, (255, 255, 255))
        screen.blit(scoreboard, (20, 20))

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.colliding(player_ship):
                print("Game Over!")
                print(f"Final Score: {int(score)}")
                sys.exit()
            for shot in shots:
                if asteroid.colliding(shot):
                    score += (100 / ASTEROID_KINDS * 
                        (ASTEROID_KINDS -
                        (asteroid.radius // ASTEROID_MIN_RADIUS - 1) / (ASTEROID_KINDS - 1)
                        * (ASTEROID_KINDS - 1)))
                    # this formula gives score inversely proportional to the size of the asteroid
                    # for example, if there are 5 sizes, the largest size will give 20 points and
                    # the smallest size will give 100 points
                    asteroid.split()
                    pygame.sprite.Sprite.kill(shot)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = (game_clock.tick(60)) / 1000
          
if __name__ == "__main__":
    main()