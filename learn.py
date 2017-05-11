# -*- coding: utf-8 -*-
# Version de Python 2.7
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
# Python te permite comentar una lineas usando un hashtag (#).
# Si quieres descomentar una linea solamente remueve el (#).
#------------------------------------------------------------------------------#

#TIPO DE DATO: NUMERO, TIPO DE VARIABLE: Entero (int)
# En python puedes hacer simples calculos como:
3+4
6*5
9-4
10/2

#Tambien podemos hacer declaraciones compuestas con los parentesis
(2+4)*(3/2)

# Si queremos guardar un valor utilizamos una variable, en este caso
x=5+6   #python guarda el valor de 11 en la variable x
y=29-13 #python guarda el valor de 16 en la variable y

print x*y # podemos usar la declaracion PRINT para demostrar diferentes valores
		  # en este caso el valor de (x) por (y) es 176
#Si queremos conocer el tipo de variable que es solamente tenemos que hacer:
print type(x) #-------> (int)
#-----------------------------------------------------------------------------#

#TIPO DE DATO: CADENA DE CARACTERES, TIPO DE VARIABLE: cadena(str)

# En python podemos usar una cadena de caracteres lo unico que tenemos que
# hacer  es escribir todo adenteo de "" comillas dobles o '' comillas simples
"Hola me llamo Daniel y tengo 22 años" # <-- esta es una cadena de caracteres

# Si queremos guardar un valor utilizamos una variable, en este caso
a="gato"
print a # podemos usar la declaracion PRINT para demostrar diferentes valores
		# en este caso el valor de (a) es gato.
#Si queremos conocer el tipo de variable que es solamente tenemos que hacer:
print type (a) #---------> (str)
#----------------------------------------------------------------------------#

# TIPO DE DATO: PUNTO FLOTANTE, TIPO DE VARIABLE: float (float)
# cuando usamos un punto en los numeros, en python se considera como una dato
# o variable tipo (float). EJEMPLO:

numero1=20.40
numero2=2.63

resultado=numero1+numero2
print resultado # podemos usar la declaracion PRINT para demostrar diferentes valores
		# en este caso el valor de (resultado) es 23.3 
#Si queremos conocer el tipo de variable que es solamente tenemos que hacer:
print type (resultado) #---------> (float)
#----------------------------------------------------------------------------#

# TIPO DE DATO: BOOLEANO, TIPO DE VARIABLE: Booleano (bool)
# cuando usamos (True o False), en python se considera como una dato
# o variable tipo (bool). EJEMPLO:

verdadero=True #NOTA: tiene que tener mayuscula T si no, no funciona.
falso=False    #NOTA: tiene que tener mayuscula F si no, no funciona.

print verdadero # podemos usar la declaracion PRINT para demostrar diferentes valores
		# en este caso el valor de (verdadero) True. 
#Si queremos conocer el tipo de variable que es solamente tenemos que hacer:
print type (verdadero) #---------> (bool)
#----------------------------------------------------------------------------#
"""
Hay mas tipos de datos y variables como listas, diccionarios, tuplas
y otros tipos mas que los veras mas adelante.
"""
#----------------------------------------------------------------------------#

"""
Esta a es una recomendacion para una buen programacion

# 1) Cuando nombres tus variables trata de usar nombres descriptivos, esto
     ayuda a que tu programa sea legible para los demas.
# 2) Cuando tu identificador(nombre de la variable) tenga mas de una palabra 
	 usa guionbajo "_" para separa las palabras. Ejemplo:
	 area_de_rectagulo=altura_de_rectangulo*ancho_de_rectangulo
"""
# Ejemplo 1
x=20
y=40
z=x*y
w=(x+y)*2
print z
print w
# Como nos damos cuenta este programa funciona pero nadie sabe que es w,x,y,z

# Ejemplo 2
altura=20
ancho=40
area=altura*ancho
perimetro=(altura+ancho)*2
print area
print perimetro
# Si corremos este programa basicamente nos da los mismos resultados pero
# ahora cuando lees el programa es mas descriptivo y es mas obvio saber lo que 
# quieres hacer.

# Ejemplo 3
# Si calificamos algunas de las palabras podemos ser mas descriptivos
# Este programa calcula el area y el perimeto de un rectangulo.
altura_de_rectangulo=20
ancho_de_rectangulo=40 
area_de_rectagulo=(altura_de_rectangulo)*(ancho_de_rectangulo)
perimetro_de_rectangulo=(altura_de_rectangulo+ancho_de_rectangulo)*2
print "El area es: ", area_de_rectagulo
print "El perimetro es: ", perimetro_de_rectangulo
# Y esto es mucho mejor para futuros debugeos y correcciones.

tu_nombre = raw_input("¿Como te llamas? ") 
print "Hola",tu_nombre
#----------------------------------------------------------------------------#
"""
=========== DECLARACIONES, ASIGNACIONES, EXPRESIONES ============
"""

#¿Que es una EXPRESION?
#- Una expresión es cualquier sección de código que evalúa a un valor.
# EJEMPLOS:

9       # Esto es una expresión porque se evalúa a un valor (9)
3+4     # 3+4 es una expresion, 3 y 4 solos se concideran subexpresiones
3+(4*5) # ¿Cuantas expresiones hay aqui?
"hola"  # Esta expresión se evalúa como "hola"
True    # Esta expresión se evalúa como True
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

#¿Que es una DECLARACION?
# es una instrucción que python puede ejecutar
# EJEMPLOS:

b=3+5     # El 3+5 es una expersion se evalua a un valor (8)
		  # pero b=3+5 es una declaracion de expersion
print (b) # print es una declaracion
if b>3 :  # if es una declaracion por que python los puede evaluar
	pass
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

#Que es una ASIGNACION?
#Es una declaracion que asocia nombres con valores en tu programa
#La forma mas simple de una declaracion de asignacion es:

numbre_de_variable="expresión" 

#para asignar una expresion a una variable simplemente usa el signo de igual =
#----------------------------------------------------------------------------#