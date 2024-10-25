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
screen.exitonclick()






 






 