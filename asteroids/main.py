# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField




def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()  # Set the frame rate to 60 FPS
    dt = 0

    # Create the sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group() 
    
    # Then set the containers for each class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots_group, updatable, drawable)

    # Create the asteroid field
    asteroid_field = AsteroidField()
    player_ = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

       

    
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)

    while True: # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        screen.fill((0, 0, 0))  # RGB value for black
        
        for asteroid in asteroids:
            if player_.collision(asteroid):
                print("Game Over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots_group:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    


        for obj in drawable:
            obj.draw(screen)
        dt = fps.tick(120)/1000  # Convert milliseconds to seconds
        
        pygame.display.flip()
    
    
        
    
     

if __name__ == "__main__":
    main()