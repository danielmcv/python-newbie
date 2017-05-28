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
y otros tipos mas que los veras mas adelante. Ver linea 197.
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

# TIPO DE DATO: LIST, TIPO DE VARIABLE: Lista (list)
# Una lista es una secuencia que contiene nuemros de objetos. Los elementos
# estan en orden y tienen un index.
# Las lista son uno de los tipos datos mas flexibles y mas usados en python
# Una lista es un contenedor que contiene numeros y otros objetos.
# Para crear una lista en python lo que tienes que hacer es poner los numeros
# o objetos dentro de corechetes [] y separalos con comas , .

# EJEMPLO:
mi_lista=["hola", 5.6, 137, True]
print type(mi_lista)

#podemos usar corchetes [] para accesar a los elementos dentro de la lista
# cada elemento tiene un index empezando desde cero[0]

#index POSITIVO
#------->    0          1         2          3           4
verduras=["Tomate", "Cebolla", "Chile", "Cilantro", "Lechuaga"]
#------->   -5         -4        -3         -2          -1        
#index NEGATIVO

#para accesar
print verduras[2] #El resultado es chile. Si usamos verduras[5 o mas ] 
# nos dara ERROR.
print verduras[-4] #EL resultado es cebolla. si usamos [-6 o menos]
# nos dara un error.



# =========== EJERCICIOS DE EXAMEN ============
age = input("How old are you? ")
days= int(age)*365
print "You are", days, "days old"

x = input("Type a number: ")
y = (int(x)**2)-(12*int(x))+11
print (y)

week_days=["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
result=input("Type a numer from 1 to 7: ")
print week_days[int(result)-1]

sample_list = [2, 10, 3, 5]
average = (sample_list[0]+sample_list[1]+sample_list[2]+sample_list[3])/4
print average

#----------------------------------------------------------------------------#
"""
=========== OPERADORES, ARITMETICA, PRECEDENCIA ============
"""


# OPPERADORES
# ¿Que son los Operadores?
# Son simbolos que le dicen al interpretador de python que haga una operacion
# logica o matematica.
3*2 #<---- El asterisco es un operador por que multiplica el 3 por el 2
7-3 #<---- Este es un operador binario por que actua a dos operandos
-7  #<---- Este esun operador unario por que actua en un operando

# TIPOS DE OPERADORES
# Matematicos: +, -, *, /, **, %, //, -
# Relacionales: <, <=, >, >=, !=, ==
# Logicos:  or, and, not
# Bitwise:  |, &, ^,~, <<,>>
# Membresia: in, not in
# Identidad: is, is not
"""
Visita esta pagina para mas info sobre los Operadores
https://www.tutorialspoint.com/python/python_basic_operators.htm
"""
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

# OPERADORES  ARITMETICO
# ¿Que es un Operador Aritmetico?
# Basicamente estos so los operadores aritmeticos, son los operadores basicos
# como sumas, restas, multiplicaciones, etc.
# -------> +, -, *, /, **, %, // <--------
# mas info aqui https://www.tutorialspoint.com/python/arithmetic_operators_example.htm

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

# PRECEDENCIA DE OPERACIONES
# ¿Que es la precedencia?
# es una regla de python que identifica que operacion se debe de realizar primero,
# EJEMPLO:


2+3-54*32 # en este caso el operador (*) se realizara primero por que 
# tiene mayor precedencia que (+)y(-)
# para ver una tabla de la precedencia de operaciones visita:
# https://www.tutorialspoint.com/python/operators_precedence_example.htm
#----------------------------------------------------------------------------#

# OPERADORES RELACIONALES

# Los operadores relacionales tambien conocidos como (operadores de comparacion)
# son los que comparan a dos operandos con otro operador,
# por ejemplo le podemos decir que si un operando es mayor o menor que otro 
# operando, etc.

# Relacionales: <, <=, >, >=, !=, == 
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

#OPERADORES LOGICOS
#logicos: and, or, not
#Ejemplo:

print 2==2 and 4>1 # el resultado seria (True) por que las dos operaciones
# son verdaderas. Si solamente una operacion fuera verdadera nor daria un 
# resultado de (False).

print 2==2 or 4>=7 # el resultado seria (True) por que una de las operaciones
# es verdadera. aqui, con que una operacion sea cierta el resultado sera (true)

print not 5>3 # el (not) es un operador unario. En este caso como el resltado
# es (True), pero si ponemos un (not), el resultado sera inverso.
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

#OPERADORES DE MEMBRESIA

# Son los operadores que determinan si hay un valor en una secuencia.
# hay solamente dos operadores de membresia.

#(in y not in) 
# (in) revisa para ver si hay un valor en una secuencia
# (not in) revisa para ver si no hay un valor en una secuencia.
# Ejemplo:
print 5 in [2,5,7,1] # El resultado es (True) por que 5 esta en la secuencia
print 5 not in [2,5,7,1] # el resultado es (False) por que 5 esta en la secuencia
#----------------------------------------------------------------------------#

"""
==================== CONDICIONALE ====================

En la programación de computadoras, declaraciones condicionales
Se utilizan para realizar diferentes cálculos o acciones dependiendo
Si la condición es Verdadero o Falso.
Recurda que (True)verdadero y (Falce)falso en Python
Se escriben con letras mayúsculas.
"""
#En la vida real todos tomamos decisiones basadas en condiciones,
#Por ejemplo podrias decir
# Si no esta lloviendo ire al parque.

# -----------Declaracion (if else)--------------#
# if expresión:
#	declaracion(s)
#	...
# else :
#	declaracion(s)
#	...
# print ("Afuera del if")

#ESTE PROGRAMA CONVIERTE LA TEMPERATURA DE CELCIUS A FAHRENHEIT
respuesta_usuario = input ("Por favor ingresa la temperatura en celcius: ")
celcius = float(respuesta_usuario)
fahrenheit = ((celcius*9)/5)+32
if fahrenheit>90:
	print ("Esta haciendo calor, compra un elado.")
else:
	print ("Que se arme la peda.")
print (fahrenheit)


#ESTE PROGRAMA AL USUARIO "QUE SI QUE ANIMAL ES SU FAVORITO" SI ESE
#ANIMAL EN UN PERRO ("dog")  QUE ARROJE ("yes") DE LO CONTRARIO QUE
#ARROJE ("no").
animal = raw_input("what animal is your favorite pet: ")
if "dog" in animal:
	print "yes"
else:
	print "no"

#ESTE PROGRAMA LE DICE AL USUARIO QUE ESCRIBA CUALQUIER NUMERO
#Y SI ESE NUMERO SE PUEDE DIVIDIR ENTRE 3 SIN DEJAR UN RESTANTE
#QUE IMPRIMA ("yes") DE LO CONTRARIO QUE IMPRIMA ("no")
number = input("type any number: ")
number = int(number%3)
if int(number) == 0:
	print "yes"
else:
	print "no"
print number

# -----------Declaracion (if elif else)--------------#
# 	EN EL CASO DE QUE NECESITES REVISAR VARIAS CONDICIONES DEBERIAS USAR
#	ESTA DECLARACION. NOTA: (elif) ES CORTO DE (else if)

#EJEMPLO:
# if expresión:
#	declaracion(s)
#	...
# elif expresión:
#	declaracion(s)
#	...
# elif expresión:
#	declaracion(s)
#	...
# else :
#	declaracion(s)
#	...
# print ("Afuera del if")

respuesta_usuario = input ("Por favor ingresa la temperatura en celcius: ")
celcius = float(respuesta_usuario)
fahrenheit = ((celcius*9)/5)+32
print "La temperatura en fahrenheit es",fahrenheit
if fahrenheit<32:
	print ("Esta congelasdo")
elif fahrenheit<50:
	print("Esta haciendo frio")
elif fahrenheit<90:
	print("Esta agusto")
else:
	print ("Pasame una bien helada por que esta haciendo calor")

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#

word = raw_input("Escribe lo que tu quieras: ")
if "dog" in word:
	print("Dog")
elif "cat" in word:
	print("Cat")
elif "cat" and "dog" in word:
	print("Dog")
else:
	print("None")

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
respuesta = input("Escribe un entero: ")
if 2 == int(respuesta):
	print("two")
elif 3 == int(respuesta):
	print("three")
elif 5 == int(respuesta):
	print("five")
else:
	print("other")

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
age = input("¿How old are you? ")
if int(age)<=0:
	print ("UNBORN")
elif int(age)>0 and int(age)<=150:
	print ("ALIVE")
else:
	print ("VAMPIRE")

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
n = input("write a number: ")
if int(n%2) == 0 and int(n%3) == 0:
	print ("BOTH")
elif int(n%2) == 0 or int(n%3) == 0:
	print ("ONE")
else:
	print ("NEITHER")

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
user_response = input("How many hours did you work this week: ")
hours = int(user_response)
if hours<0 or hours>168:
	print ("INVALID")
elif hours<=40:
	hours = hours*8
	print "YOU MADE", hours, "DOLLARS THIS WEEK"
