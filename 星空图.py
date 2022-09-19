import turtle
from random import randint

def draw_star():
  # 画笔的颜色
    turtle.pencolor('blue')
    turtle.hideturtle()
  #填充星星的颜色
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range(5):
      turtle.forward(50)
      turtle.right(144)
    turtle.end_fill()

# 将 ??? 改成你想画的星星个数
for i in range(38):
  turtle.speed(0)
  turtle.penup()
  x = randint(-150, 150)
  y = randint(-100, 100)
  turtle.goto(x, y)
  turtle.pendown()
  draw_star()
  turtle.end_fill()

turtle.penup()
turtle.goto(0, -130)
turtle.pendown()
turtle.write('一闪一闪亮晶晶',  font = ('SimHei', 12, 'bold'))
turtle.done()