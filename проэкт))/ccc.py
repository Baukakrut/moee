


import turtle
import random

# Настройки окна
screen = turtle.Screen()
screen.bgcolor("black")

# Создаем черепашку для рисования
t = turtle.Turtle()
t.speed(0)  # Максимальная скорость рисования

# Функция для рисования звезд
def draw_star(size, color):
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# Рисуем звезды
num_stars = 50
for _ in range(num_stars):
    x = random.randint(-screen.window_width()//2, screen.window_width()//2)
    y = random.randint(-screen.window_height()//2, screen.window_height()//2)
    size = random.randint(5, 20)
    color = random.choice(["white", "yellow", "lightyellow", "azure", "lightcyan"])
    t.penup()
    t.goto(x, y)
    t.pendown()
    draw_star(size, color)

# Рисуем луну
t.penup()
t.goto(-200, 100)
t.pendown()
t.color("lightyellow")
t.begin_fill()
t.circle(50)
t.end_fill()

# Завершаем программу по клику на окно

import turtle
import math
# Настройки окна черепахи
screen = turtle.Screen()
screen.bgcolor("black")

# Создание черепахи
sun = turtle.Turtle()
sun.shape("triangle")
sun.color("yellow")
sun.speed(0)  # Максимальная скорость рисования

# Функция для рисования "лучей" солнца
def draw_sun_rays():
    sun.penup()
    sun.goto(100, 100)
    sun.pendown()
    sun.left(90)
    ray_length = 100
    for _ in range(36):
        sun.forward(ray_length)
        sun.backward(ray_length)
        sun.right(10)

# Функция для рисования круга солнца
def draw_sun_circle():
    sun.penup()
    sun.goto(0, 0)
    sun.pendown()
    sun.circle(1)

# Рисуем солнце
draw_sun_rays()
draw_sun_circle()



# Создание черепахи
sun = turtle.Turtle()
sun.shape("triangle")
sun.color("green")
sun.speed(0)  # Максимальная скорость рисования

# Функция для рисования "лучей" солнца
def draw_sun_rays():
    sun.penup()
    sun.goto(200, 200)
    sun.pendown()
    sun.left(90)
    ray_length = 100
    for _ in range(36):
        sun.forward(ray_length)
        sun.backward(ray_length)
        sun.right(10)

# Функция для рисования круга солнца
def draw_sun_circle():
    sun.penup()
    sun.goto(0, 0)
    sun.pendown()
    sun.circle(1)

# Рисуем солнце
draw_sun_rays()
draw_sun_circle()



# Создание черепахи
sun = turtle.Turtle()
sun.shape("triangle")
sun.color("pink")
sun.speed(0)  # Максимальная скорость рисования

# Функция для рисования "лучей" солнца
def draw_sun_rays():
    sun.penup()
    sun.goto(400, 300)
    sun.pendown()
    sun.left(90)
    ray_length = 100
    for _ in range(36):
        sun.forward(ray_length)
        sun.backward(ray_length)
        sun.right(10)

# Функция для рисования круга солнца
def draw_sun_circle():
    sun.penup()
    sun.goto(0, 400)
    sun.pendown()
    sun.circle(1)

# Рисуем солнце
draw_sun_rays()
draw_sun_circle()

# 

# Настройки окна черепахи
screen = turtle.Screen()
screen.bgcolor("black")

# Создание черепахи
sun = turtle.Turtle()
sun.shape("triangle")
sun.color("violet")
sun.speed(0)  # Максимальная скорость рисования

# Функция для рисования "лучей" солнца
def draw_sun_rays():
    sun.penup()
    sun.goto(250, 200)
    sun.pendown()
    sun.left(90)
    ray_length = 100
    for _ in range(36):
        sun.forward(ray_length)
        sun.backward(ray_length)
        sun.right(10)

# Функция для рисования круга солнца
def draw_sun_circle():
    sun.penup()
    sun.goto(200, 150)
    sun.pendown()
    sun.circle(1)

# Рисуем солнце
draw_sun_rays()
draw_sun_circle()







# Создание черепахи
sun = turtle.Turtle()
sun.shape("triangle")
sun.color("red")
sun.speed(0)  # Максимальная скорость рисования

# Функция для рисования "лучей" солнца
def draw_sun_rays():
    sun.penup()
    sun.goto(300, 100)
    sun.pendown()
    sun.left(90)
    ray_length = 100
    for _ in range(36):
        sun.forward(ray_length)
        sun.backward(ray_length)
        sun.right(10)

# Функция для рисования круга солнца
def draw_sun_circle():
    sun.penup()
    sun.goto(0, 50)
    sun.pendown()
    sun.circle(1)

# Рисуем солнце
draw_sun_rays()
draw_sun_circle()


# Создание черепахи
sun = turtle.Turtle()
sun.shape("triangle")
sun.color("blue")
sun.speed(0)  # Максимальная скорость рисования

# Функция для рисования "лучей" солнца
def draw_sun_rays():
    sun.penup()
    sun.goto(-20, 400)
    sun.pendown()
    sun.left(90)
    ray_length = 100
    for _ in range(36):
        sun.forward(ray_length)
        sun.backward(ray_length)
        sun.right(10)

# Функция для рисования круга солнца
def draw_sun_circle():
    sun.penup()
    sun.goto(350, 0)
    sun.pendown()
    sun.circle(1)

# Рисуем солнце
draw_sun_rays()
draw_sun_circle()


# Создание черепахи
sun = turtle.Turtle()
sun.shape("triangle")
sun.color("violet")
sun.speed(0)  # Максимальная скорость рисования

# Функция для рисования "лучей" солнца
def draw_sun_rays():
    sun.penup()
    sun.goto(-300, 100)
    sun.pendown()
    sun.left(90)
    ray_length = 100
    for _ in range(36):
        sun.forward(ray_length)
        sun.backward(ray_length)
        sun.right(10)

# Функция для рисования круга солнца
def draw_sun_circle():
    sun.penup()
    sun.goto(0, 0)
    sun.pendown()
    sun.circle(1)

# Рисуем солнце
draw_sun_rays()
draw_sun_circle()


sun = turtle.Turtle()
sun.shape("triangle")
sun.color("orang")
sun.speed(0)  # Максимальная скорость рисования

# Функция для рисования "лучей" солнца
def draw_sun_rays():
    sun.penup()
    sun.goto(-200, 100)
    sun.pendown()
    sun.left(90)
    ray_length = 100
    for _ in range(36):
        sun.forward(ray_length)
        sun.backward(ray_length)
        sun.right(10)

# Функция для рисования круга солнца
def draw_sun_circle():
    sun.penup()
    sun.goto(0, 0)
    sun.pendown()
    sun.circle(1)

# Рисуем солнце
draw_sun_rays()
draw_sun_circle()


sun = turtle.Turtle()
sun.shape("triangle")
sun.color("red")
sun.speed(0)  # Максимальная скорость рисования

# Функция для рисования "лучей" солнца
def draw_sun_rays():
    sun.penup()
    sun.goto(-50, 50)
    sun.pendown()
    sun.left(90)
    ray_length = 100
    for _ in range(36):
        sun.forward(ray_length)
        sun.backward(ray_length)
        sun.right(10)

# Функция для рисования круга солнца
def draw_sun_circle():
    sun.penup()
    sun.goto(0, 0)
    sun.pendown()
    sun.circle(1)

# Рисуем солнце
draw_sun_rays()
draw_sun_circle()


sun = turtle.Turtle()
sun.shape("triangle")
sun.color("pink")
sun.speed(0)  # Максимальная скорость рисования

# Функция для рисования "лучей" солнца
def draw_sun_rays():
    sun.penup()
    sun.goto(-350, 50)
    sun.pendown()
    sun.left(90)
    ray_length = 100
    for _ in range(36):
        sun.forward(ray_length)
        sun.backward(ray_length)
        sun.right(10)

# Функция для рисования круга солнца
def draw_sun_circle():
    sun.penup()
    sun.goto(-200, 200)
    sun.pendown()
    sun.circle(1)

# Рисуем солнце
draw_sun_rays()
draw_sun_circle()




sun.hideturtle()
turtle.done()
screen.exitonclick()