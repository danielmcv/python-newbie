# -*- coding: utf-8 -*-
"""
============ VARIABLES Y IDENTIFICADORES ============
En el mundo de la programacion es sumamente importante
entender que es una variable y un identificador.

Entonces...
¿Que es una variable?
Las variables son locaciones reservadas en la memoria 
de una computadora para almacenar un valor.
Puedes almacenar diferentes tipos de datos, tales como,
numeros, enteros, coma flotantes, una cadena de caracteres, etc.

si no conoces los tipos de datos, no te preocupes lo veremos
mas adelante.

El lenguage de programacion python automaticamente asigna (reserva)
un espacio en la memoria por cada variable

¿Que es un identificador?
Es el nombre que se le da a una variable o a otras entidades tales
como, funciones, objetos, etc.

#### IMPORTANTE ####
No confundas una variable con un identificador. Recuerda que un
identificador es el nombre que se le da a una variable y una variable
tiene otras propiedades como valor, tipo, alcance.
####################

EJEMPLO: 
imaginate a una persona como una variable. Esta persona tiene un 
nombre<--(identificador) pero tambien tiene otras propiedades tales
como altura, peso, color de ojos, etc.


Como nombrar a tus identificadores:
1---> es importante saber que los identificador distinguen 
	  mayusculas y minusculas (R es diferente a r).
2---> Solo pueden contener letras, numeros y guinbajo. no pueden 
	  contener signo de dinero ($) ni signos de matematica como 
	  (+, -, %, *, /,etc.).
3---> no pueden empezar con un numero, ejemplo (2numero)<-- esto es mal.
4---> no pueden ser lo mismo a los python (keywords). Referencia >>> 
	  https://www.programiz.com/python-programming/keyword-list
VALIDOS >>> abc, Abc, _x5, my_x, my_x1. <<<<<<
INVALIDOS >>>> 2x, x.2, A-2, my x, for. <<<<<<
"""
tu_nombre = raw_input("¿Como te llamas? ") 
print"Hola",tu_nombre