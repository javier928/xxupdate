# Flavio
# Vamos a hacer un programa que realiza un segundo test de CUATRO preguntas sobre
# Microsoft windows,CMS,Wordpress y Tiendas Virtuales en España
# Un CMS (Sistema de Gestion de Contenidos) es una herramienta que permite
# crear y administrar contenido digital sin necesidad de saber programar.
# WordPress.com es una plataforma de blogging y creación de
# sitios web basada en el CMS Wordpress, pero alojada y gestionada por
# WordPress, lo que facilita su uso y mantenimiento.


# Definición de funciones

def examen2():
    puntos=0

    #PREGUNTA 1
    A="virtual,no es necesario comunicar la apertura  a la Agencia Tributaria. (V/F)?:"
    xxx = input("Si no se tienen los beneficios en el primer mes de actividad de una tienda," +A)
    if xxx=="F":
        print("Respuesta correcta. Tienes 1 punto.")
        puntos=puntos+1
    #endif

    #PREGUNTA 2
    A="autónomo en España está ligada a la habitualidad y la finalidad lucrativa de la: "
    B="actividad o grado de discapacidad? "
    xxx = input("""Completa la frase: La obligación de darse de alta como """+A+B)
    if xxx=="actividad":
        print("Respuesta correcta.Tienes 1punto.")
        puntos=puntos+1
    #endif

    #PREGUNTA 3
    A="ha sido publicado con wordpress.com correctamente, debemos visitar la "
    B="direccion "
    C="Siguiente:"
    F=A+B+C
    xxx = input("""Completa la frase: Para comprobar que nuestro sitio web  """+F)
    if xxx=="https://wordpress.com/sites":
        print("Respuesta correcta. Tienes 1 punto.")
        puntos=puntos+1
    #endif

    #PREGUNTA 4
    A="permite crear y administrar  "
    B="contenido digital "
    C="sin necesidad de saber... PISTA: ¿programar o sumar?"
    F=A+B+C
    xxx = input("""Completa la frase: Un CMS (Sistema de Gestión de Contenidos) es una herramienta que  """+F)
    if xxx=="programar":
        print("Respuesta correcta. Tienes 1 punto.")
        puntos=puntos+1
    #endif

    print("Tu nota final es:")
    print(puntos)

    #Main Program

xName = input("Dime tu nombre, por favor:")
print("Hola, " + xName + "!")
A="Vamos a hacer un test de dos preguntas sobre "
B="Microsoft windows, CMS, WordPress y "
C="Tiendas Virtuales en España. "
F=A+B+C
print(F)
examen2()
print("Fin  de la prueba.")