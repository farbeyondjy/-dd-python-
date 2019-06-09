# coding=utf-8
import sys
import pygame
import random

from pygame.locals import *

width = 700
height = 700
blue = (0, 0, 255)
snake_speed = 5
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
dark_blue = (0, 0, 139)
cell_size = 20
map_width = int(width / cell_size)
map_height = int(height / cell_size)
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
HEAD = 0


def draw_snake(screen, snake_coords):
    for coord in snake_coords:
        x = coord['x'] * cell_size
        y = coord['y'] * cell_size
        wormSegmentRect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(screen, dark_blue, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, cell_size - 8, cell_size - 8)
        pygame.draw.rect(screen, blue, wormInnerSegmentRect)


def draw_food(screen, food):
    x = food['x'] * cell_size
    y = food['y'] * cell_size
    foodRect = pygame.Rect(x, y, cell_size, cell_size)
    pygame.draw.rect(screen, red, foodRect)


def get_random_location():
    return {'x': random.randint(0, map_width - 1), 'y': random.randint(0, map_height - 1)}


def move_snake(direction, snake_coords):
    global newHead
    if direction == UP:
        newHead = {'x': snake_coords[HEAD]['x'], 'y': snake_coords[HEAD]['y'] - 1}
    elif direction == DOWN:
        newHead = {'x': snake_coords[HEAD]['x'], 'y': snake_coords[HEAD]['y'] + 1}
    elif direction == LEFT:
        newHead = {'x': snake_coords[HEAD]['x'] - 1, 'y': snake_coords[HEAD]['y']}
    elif direction == RIGHT:
        newHead = {'x': snake_coords[HEAD]['x'] + 1, 'y': snake_coords[HEAD]['y']}

    snake_coords.insert(0, newHead)


def terminate():
    pygame.quit()
    sys.exit()


def show_start_info(screen):
    font = pygame.font.Font('myfont.ttf', 40)
    tip = font.render("按任意键开始游戏~~~", True, (65, 105, 225))
    gamestart = pygame.image.load("snake.jpg")
    gamestartrect = gamestart.get_rect()
    screen.blit(gamestart, gamestartrect)
    screen.blit(tip, (240, 550))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                else:
                    return


def show_end_info(screen):
    font = pygame.font.Font("myfont.ttf", 40)
    tip1 = font.render("按Q或者ESC退出游戏, ", True, (0, 255, 0))
    tip2 = font.render("按任意键重新开始游戏~", True, (0, 255, 0))
    gamestart = pygame.image.load("end.jpg")
    screen.blit(gamestart, (0, 0))
    screen.blit(tip1, (150, 600))
    screen.blit(tip2, (150, 650))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    terminate()
                else:
                    return


def snake_is_eat_food(snake_coords, food):
    if snake_coords[HEAD]['x'] == food['x'] and snake_coords[HEAD]['y'] == food['y']:
        food['x'] = random.randint(0, map_width - 1)
        food['y'] = random.randint(0, map_height - 1)
    else:
        del snake_coords[-1]


def snake_is_alive(snake_coords):
    tag = True
    if snake_coords[HEAD]['x'] == -1 or snake_coords[HEAD]['x'] == map_width or snake_coords[HEAD]['y'] == -1 or \
            snake_coords[HEAD]['y'] == map_height:
        tag = False
    for snake_body in snake_coords[1:]:
        if snake_body['x'] == snake_coords[HEAD]['x'] and snake_body['y'] == snake_coords[HEAD]['y']:
            tag = False
    return tag


def draw_score(screen, score):
    font = pygame.font.Font("myfont.ttf", 30)
    score1 = font.render("得分: %s" % score, True, green)
    scoreRect = score1.get_rect()
    scoreRect.topleft = (width - 120, 10)
    screen.blit(score1, scoreRect)


def main():
    pygame.init()
    snake_speed_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    screen.fill(white)
    pygame.display.set_caption("Python 贪吃蛇小游戏")
    show_start_info(screen)

    while True:
        running_game(screen, snake_speed_clock)
        show_end_info(screen)


def running_game(screen, snake_speed_clock):
    startx = random.randint(3, map_width - 8)
    starty = random.randint(3, map_height - 8)
    snake_coords = [{'x': startx, 'y': starty},
                    {'x': startx - 1, 'y': starty},
                    {'x': startx - 2, 'y': starty}]

    direction = RIGHT
    food = get_random_location()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        move_snake(direction, snake_coords)

        result = snake_is_alive(snake_coords)
        if not result:
            break

        background = pygame.image.load("ground.jpg")
        screen.blit(background, (0, 0))
        snake_is_eat_food(snake_coords, food)
        draw_snake(screen, snake_coords)
        draw_food(screen, food)
        draw_score(screen, len(snake_coords) - 3)
        pygame.display.update()
        snake_speed_clock.tick(snake_speed)


main()
