import random
import os
import time

diccionario = {"Litio":"1","Sodio":"1","Potasio":"1","Rubidio":"1","Cesio":"1","Francio":"1","Plata":"1","Amonio":"1","Berilio":"2","Magnesio":"2","Calcio":"2","Estroncio":"2","Bario":"2","Radio":"2","Cinc":"2","Cadmio":"2","Aluminio":"3","Cobre":"1,2","Mercurio":"1,2","Oro":"1,3","Cromo":"2,3","Manganeso":"2,3","Hierro":"2,3","Cobalto":"2,3","Niquel":"2,3","Estannio":"2,4","Plomo":"2,4","Platino":"2,4","Paladio":"2,4","Hidrogeno":"1,-1","Fluor":"1,-1","Cloro":"1,3,5,7,-1","Bromo":"1,3,5,7,-1","Yodo":"1,3,5,7,-1","Oxigeno":"-2","Azufre":"2,4,6,-2","Selenio":"2,4,6,-2","Teluro":"2,4,6,-2","Nitrogeno":"1,3,5,-3","Fosforo":"1,3,5,-3","Arsenico":"1,3,5,-3","Antimonio":"1,3,5,-3","Boro":"3,-3","Bismuto":"3,5,-3","Carbono":"2,4,-4","Silicio":"4,-4"}
k, v = random.choice(list(diccionario.items()))

os.system('cls')
print('''-----------------------------------------------------------
ATENCION
-----------------------------------------------------------
Cabe recalcar que las valencias que aparecen aqui son las que estoy 
dando en mi curso.Obviamente hay mas pero como no me las piden pues 
no las pongo.Si tienes que estudiar mas valencias puedes editar este 
archivo y aniadir las valencias que necesites en la variable diccionario.
Ejemplo > "Oro","1,3"
De esa forma aniadiras ese elemento al programa\n\nOtra cosa tambien importante,si un elemento tiene mas de una valencia
como por ejemplo el Nitrogeno,tienes que poner sus valencias de 
izquierda a derecha\n\nEjemplo:1,3,5\n\nY si tiene valencias negativas como el azufre tienes que ponerlas
tambien de izquierda a derecha\n\nEjemplo:2,4,6,-2\n\n''')

input("Pulsa ENTER para continuar....")
os.system('cls')

score = 0
bad_score = 0

while True:
    k, v = random.choice(list(diccionario.items()))

    respuesta = input("Introduce las valencias del {} > ".format(k))

    if respuesta == v:
        print("\nCorrecto\n")
        score += 1
        print("Bien : {}\nMal : {}".format(score, bad_score))
        time.sleep(1.5)
        os.system('cls')
    else:
        print("\nMal,el {} tiene las valencias {}\n".format(k, v))
        bad_score += 1
        print("Bien : {}\nMal : {}".format(score, bad_score))
        time.sleep(4)
        os.system('cls')