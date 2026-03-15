import turtle
import time
import random

janela = turtle.Screen()
janela.bgcolor("lightgreen")
janela.setup(width=600, height=600)
janela.tracer(0)

cabeca = turtle.Turtle()
cabeca.speed(0)
cabeca.shape("square")
cabeca.color("blue")
cabeca.penup()
cabeca.goto(0,0)
cabeca.direction = "stop"

def ir_para_cima():
    cabeca.direction = "up"

def ir_para_baixo():
    cabeca.direction = "down"

def ir_para_esquerda():
    cabeca.direction = "left"

def ir_para_direita():
    cabeca.direction = "right"

janela.listen()

janela.onkeypress(ir_para_cima, "w")
janela.onkeypress(ir_para_baixo, "s")
janela.onkeypress(ir_para_esquerda, "a")
janela.onkeypress(ir_para_direita, "d")

def mover():
    if cabeca.direction == "up":
        y = cabeca.ycor()
        cabeca.sety(y + 20)

    if cabeca.direction == "down":
        y = cabeca.ycor()
        cabeca.sety(y - 20)

    if cabeca.direction == "right":
        x = cabeca.xcor()
        cabeca.setx(x + 20)

    if cabeca.direction == "left":
        x = cabeca.xcor()
        cabeca.setx(x - 20)

comida = turtle.Turtle()
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

segmentos = []

while True:
    janela.update()

    if cabeca.xcor() > 290 or cabeca.xcor() < -290 or cabeca.ycor() > 290 or cabeca.ycor() < -290:
        time.sleep(1)
        cabeca.goto(0, 0)
        cabeca.direction = "stop"
        for segmento in segmentos:
            segmento.goto(1000, 1000)
        segmentos.clear() 

    if cabeca.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        novo_segmento = turtle.Turtle()
        novo_segmento.speed(0)
        novo_segmento.shape("square")
        novo_segmento.color("blue") 
        novo_segmento.penup()
        segmentos.append(novo_segmento)
    
    for index in range(len(segmentos) - 1, 0, -1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x, y)

    if len(segmentos) > 0:
        x = cabeca.xcor()
        y = cabeca.ycor()
        segmentos[0].goto(x, y)
    
    mover()
    time.sleep(0.1)
