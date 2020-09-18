####Fernando Rodriguez - A01194932 (ferrdz99)####
####Jose de Jesús Ortiz Rangel - A01611006 (JoseOrtizR)####
#Librerias utilizadas para el codigo
from random import randrange
from turtle import *
from freegames import vector
#Definicion de variables
ball = vector(-200, -200) #La pelota
speed = vector(0, 0) #Velocidad
targets = [] #Aqui se hace matriz, se van agregando con appends en la funcion "Move"

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        #Se le da una posición de lanzamiento al proyectil; esta se encuentra en la esquina inferior izquierda.
        ball.x = -199
        ball.y = -199
        #Se definen algunas velocidades iniciales 
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25
#Regresa un valor booleano dependiendo de la posición de xy; para ser verdadero debe de estar dentro de los límites de la ventana
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)#Se genera un valor aleatorio para las y
        target = vector(200, y)# Se genera un balón en el borde derecho del plano con la coordenada y definida por el valor recien conseguido
        targets.append(target)# Se añade este nuevo objetivo a la lista de objetivos 

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35#Se define una nueva velocidad para las y
        ball.move(speed)#Se mueve el proyectil tomando como argumento el vector velocidad.

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()


#En esta parte se modifica la velocidad de los proyectiles y la de los balones.
#La función ontimer() es un temporizador que llama a la función move en un periodo
#determinado. Para hacer todo más rápido, basta con reducir el tiempo de espera.
    
#Se define un factor que determinará la magnitud de la velocidad
    n=5
#Se modifica la velocidad inicial multiplicando el segundo argumento de ontimer()
#por el inverso multiplicativo del factor n
    ontimer(move, int(50*(1/n)))

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
