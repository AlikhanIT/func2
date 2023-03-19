import pygame
import time
import random

pygame.init()

# Установить цветовые переменные, используя значения RGB
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Установка размера дисплея
dis_width = 600
dis_height = 400

# Создание окна отображения игры и установка заголовока
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('ЛАБ8 и СРС')

# Установка игровых часов
clock = pygame.time.Clock()

# Установка размера каждого змеиного блока и скорости движения змеи
snake_block = 10
snake_speed = 15

# Установка стиля шрифта для отображения результатов и сообщения об окончании игры
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Функция для отображения оценки
def Your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# Функция для рисования змеи
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Функция для отображения сообщения об окончании игры
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Основная функция игрового цикла
def gameLoop():
    # Установка флага game over и game close False
    game_over = False
    game_close = False

    # Установка начального положения головы змеи в центре дисплея
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Установка начального положения изменение головы змеи на 0
    x1_change = 0
    y1_change = 0

    # Создание пустого списка для хранения координат блоков змеи
    snake_List = []
    # Установка начальной длины змеи равной 1 блоку
    Length_of_snake = 2

    # Произвольная установка положения ягоды на дисплее
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Основной игровой цикл
    while not game_over:

        # Если флаг "game_close" имеет значение True, отобразите сообщение "игра окончена" и счет и разрешите игроку играть снова или выйти из игры
        while game_close == True:
            dis.fill(blue)
            message("Ты проиграл! Нажмите C-Перерождение еще раз или Q-Выход", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Обработка события (ввод с клавиатуры, закрытие окна)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка не сталкивается ли змея сама с собой
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Рисование змеи
        our_snake(snake_block, snake_List)

        # Показать счет
        Your_score(Length_of_snake - 1)

        # Обновите дисплей
        pygame.display.update()

        # Если змея съест еду то создаётся новая и увеличивается длина змеи
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Контроль скорости змеи
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()