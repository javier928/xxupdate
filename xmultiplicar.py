
# definicion de funciones

def examen():
    puntos=0
    #PREGUNTA 1
    xxx = input("El comando COPY en Windows sirve para copiar archivos. (V/F)?: ")
    if xxx=="V":
        print("Respuesta correcta. Tienes 1 punto.")
        puntos=puntos+1
    #endif
    #PREGUNTA 2
    A="imprimir el cuadrado de la variable X en pantalla: print o print(X*X) ?"
    xxx = input("""Cual es la orden que debemos teclear para """+A)
    if xxx=="print(X*X)":
        print("Respuesta correcta. Tienes 1 punto.")
        puntos=puntos+1
    #endif
    print("Tu nota final es:")
    print(puntos)



##### programa principal (main program)

xname = input("Dime tu nombre, por favor: ")
print("Hola, " + xname + "!")
a="Vamos a hacer un test dos preguntas sobre"
b=" Microsoft Windows."
print(a+b)
examen()
print("Fin de la prueba.")


