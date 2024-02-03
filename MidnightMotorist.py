import pygame
from pygame.locals import *
import random

size = width, height =(960, 540)
road_h = int(height/1.6)
roadmark_h = int(height/80)
road_w = int(width/1.6)
roadmark_w = int(width/80)
lane_2 = height/2 - road_h/4
lane_3 = height/2 + road_h/4
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4

pygame.init();
running = True;
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")
screen.fill((60, 220, 0))

pygame.display.update()

#images
road = pygame.image.load('FNAF_MidnightMotorist_Assets/Road.png')
#car 1
car = pygame.image.load('FNAF_MidnightMotorist_Assets/MainCar.png')
car_loc = car.get_rect()
car_loc.center = right_lane, lane_2
#car 2
car2 = pygame.image.load('FNAF_MidnightMotorist_Assets/CarRight.png')
car2_loc = car2.get_rect()
car2_loc.center = 960, lane_3

counter = 0
speed = 1

while running:

    counter += 1
    if counter == 1000:
        speed += 0.05
        counter = 0
        print("level up", speed)
    #enemy
    car2_loc[0] -= speed
    if car2_loc[0] <= 0:
        car2_loc[0] = width
        if random.randint(0, 1) == 0:
            car2_loc.center = width, lane_2
        else:
            car2_loc.center = width, lane_3
    #end game
    if car_loc[1] == car2_loc[1] and car2_loc[0] > car_loc[0] - 135:
        print("Game over")
        break
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_w, K_UP]:
                car_loc = car_loc.move(0, -int(road_h/2))
            if event.key in [K_s, K_DOWN]:
                car_loc = car_loc.move(0, int(road_h/2))
    
    screen.blit(road, (0, 0))
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()

pygame.quit();