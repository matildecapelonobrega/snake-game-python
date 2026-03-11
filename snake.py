import turtle
import time

#fundo do jogo
janela = turtle.Screen()
janela.bgcolor("lightgreen")
janela.setup(width=600, height=600)

#a cabeca da cobra
cabeca = turtle.Turtle()
cabeca.speed(0)
cabeca.shape("square")
cabeca.color("blue")
cabeca.penup()
cabeca.goto(0,0)
cabeca.direction = "stop"

#teclado 
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

#movimentos da cobra
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

#loop
while True:
    janela.update()
    mover()
    time.sleep(0.1)

turtle.done()

