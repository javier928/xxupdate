###################################################################
#
# Programa xsuma1.py desarrollado en Python 3 en Windows 10
#
# El script visualiza el primer registro de la tabla page1 y
#
# permite su modificacion mediante la entrada de una cadena nueva:
#
# newline1
#
# El primer registro de la tabla page1 contiene un parrafo largo
#
# de la primera pagina del libro o un nombre de una persona
#
# Como construir la cadena para pasarla como orden SQLite?
#
# La base de datos se llama test11.db. Puede descargar el archivo .db visitando:
#
# https://github.com/javier928/xxupdate
#
# La tabla 1 se llama page1. La tabla contiene parrafos de un libro o preguntas de un test
#
# La tabla 1 (y cada tabla de la bd solo contiene 1 registro. Cada registro contiene los parrafos de esa pag)
#
# La tabla 2 se llama page2. La tabla contiene mas parrafos del libro o mas preguntas de un test.
#
# La tabla 9 se llama page9.La tabla contiene mas parrafos del libro.El libro contiene 10 paginas (10 tablas).
#
# La tabla tiene los siguientes campos (todos son tipo texto excepto booknn y pagenn, que son numericos):
#
# line1, line2...line20
#
# Que campo estamos utilizando para filtrar registros? pagenn
#
# Por que debemos construir un string para ejecutar la orden SQL?
#
###################################################################
import os
import sqlite3
import tabulate

def cls():
    os.system("cls")

def superprint(ppp,qqq):
	##si ppp es '1' se imprime una linea en blanco antes de imprimir el valor de qqq
	if ppp=="1":
		print(" ")
	print(qqq)

def printlongline():
    print("--------------------------------------------------------------------------------------------")

## preguntamos que (ebook) queremos abrir:
## el user puede elegir entre test1.db or test2.db
cls()
superprint("0"," Welcome to SQL database editor lite")
print(" ")
zx= input(" Which database do you want to work with? <Enter 0 to exit, enter 1 for test11.db> ")

conn= sqlite3.connect("test11.db")
print(" ")
print(" SQLite database <test11.db> successfully opened. ")

## preguntamos que TABLE (page of the book) queremos ACTUALIZAR
print(" ")
Xplineyyy= input(" Which (TABLE or PAGE) number do you want to view? <Enter 0 to exit> ")
Xpyyy=int(Xplineyyy)

## construimos orden SQLite para contar registros en la tabla 1. SELECT field1,field2,etc. from table1 (or page1)
cursor1= "SELECT LINE1,"
cursor2= "LINE2, LINE3, LINE4, LINE5,LINE6, LINE7, LINE8, LINE9,LINE10,LINE11, LINE12, LINE13,LINE14,LINE15,LINE16, LINE17, LINE18, LINE19,LINE20, PAGENN, "
cursor3= "LINE1N, LINE2N, LINE3N FROM PAGE"+Xplineyyy
cursor= conn.execute(cursor1+cursor2+cursor3)

cursor1= "SELECT COUNT(*)"
cursor2= " "
cursor3= "FROM PAGE"+Xplineyyy
#page1 is table1 in sqlite database test.db
cursor= conn.execute(cursor1+cursor2+cursor3)

print(" ")
plineyyy= input(" Which (record) number do you want to edit? <Enter 0 to exit, 999 for more help> ")
pyyy=int(plineyyy)

### falta cambiar el filtro en la orden SELECT para mostrar pagenn= plineyyy
cursor1= "SELECT LINE1,"
cursor2= "LINE2, LINE3, LINE4, LINE5, LINE6, LINE7, LINE8, LINE9,LINE10,LINE11, LINE12, LINE13,LINE14,LINE15,LINE16, LINE17, LINE18, LINE19,LINE20,PAGENN, "
cursor3= "LINE1N, LINE2N, LINE3N FROM PAGE"+Xplineyyy+" "
cursor4= "WHERE PAGENN="+plineyyy+" "
cursor= conn.execute(cursor1+cursor2+cursor3+cursor4)

cls()
for row in cursor:
	print("--------------------------------------------------------------------------------------------\n")
	print(" Fields:     Content:")
	print("--------------------------------------------------------------------------------------------\n")
	print(" line1:     ", row[0].strip(),"gasta "+str(row[21])+" eur")
	print(" line2:     ", row[1].strip(),"gasta "+str(row[22])+" eur")
	print(" line3:     ", row[2].strip(),"gasta "+str(row[23])+" eur")
	print(" line4:     ", row[3])
	print(" line5:     ", row[4])
	print(" line6:     ", row[5])
	print(" line7:     ", row[6])
	print(" line8:     ", row[7])
	print(" line9:     ", row[8])
	print(" line10:    ", row[9])
	print(" line11:    ", row[10])
	print(" line12:    ", row[11])
	print(" line13:    ", row[12])
	print(" line14:    ", row[13])
	print(" line15:    ", row[14])
	print(" line16:    ", row[15])
	print(" line17:    ", row[16])
	print(" line18:    ", row[17])
	print(" line19:    ", row[18])
	print(" line20:    ", row[19],"Total: "+str(row[21]+row[22]+row[23])+" eur")
	print(" pagenn:    ", row[20])
	print("\n--------------------------------------------------------------------------------------------")

conn.close()
