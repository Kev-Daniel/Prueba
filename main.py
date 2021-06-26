import numpy as np
from numpy.core.fromnumeric import prod
import math 
#Creacion de una funcion respuesta
ced=[]
def separacion(cedula):
    for i in cedula:
        ced.append(int(i))
    print(ced)
def respuesta():
    R_correcta=False
    num=0
    while(not R_correcta):
        try:
            num = int(input("Introduce la opcion que deseas: "))
            R_correcta=True
        except ValueError:
            print('Opcion incorrecta vuelve a selecionar')
     
    return num
salir = False
opcion = 0
#Creacion del Menu
while not salir:
    #Creacion del array de la cedula
    in_cedula=input("Ingresa tu cedula: ")
    separacion(in_cedula)
    dimensiones=(100 , 100)
    array=np.ones((dimensiones))
    print("Matriz 100x100")
    print(array)
    filas=len(array)
    columnas=len(array[0])
  
    print ("\t\t\t\t\tBIENVENIDO AL MENU")
    print ("1. Sumar los elementos de una determinada columna")
    print ("2. Sumar los elementos de una determinada fila")
    print ("3. Sumar los elementos de las diagonales")
    print ("4. Multiplicar los elementos de una determinada columna")
    print ("5. Multiplicar los elementos de una determinada fila")
    print ("6. Multiplicar los elementos de las diagonales.")
    print ("7. Salir")
     
    print ("Elige una opcion")
    
    opcion = respuesta()
 
    if opcion == 1:
        fila=input("Ingrese el numero de fila que desea sumar: ")
        for fila in range(filas):
            suma= sum(array[fila])
        print ("\n\n")
        print("Respuesta de la suma: ", suma)
        
    elif opcion == 2:
        colum=input("Ingrese el numera de columna que desea sumar:")
        for colum in range(columnas):
            suma= sum([filas[colum] for filas in array ])
        print ("\n\n")
        print("Respuesta de la suma:", suma)
        
    elif opcion == 3:
        print("suma de las diagonales")
    elif opcion == 4:
        fila_mul=input("Ingrese la fila que desea multiplicar:")
        for fila_mul in range(filas):
            multi= math.prod(array[fila_mul])
        print ("\n\n")
        print("Respuesta de la multiplicación:", multi)
      
    elif opcion == 5:
        colum_mul=input("Ingrese el numera de columna que desea sumar:")
        for colum_mul in range(columnas):
            multi= math.prod([filas[colum_mul] for filas in array ])
        print ("\n\n")
        print("Respuesta de la multiplicación:", multi)
       
    elif opcion == 6:
        print("Multiplicacion de las diagonales")
    elif opcion == 7:
        salir = True
    else:
        print ("Elije una opcion del 1 al 7")
