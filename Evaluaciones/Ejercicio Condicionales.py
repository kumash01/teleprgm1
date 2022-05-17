#Ejercicio1
def calculodearea():
  from math import pi
  radio = float(input("Indique el radio de la circunferencia "))
  area= pi * radio**2   
  print("El círculo tiene un área de:",area)
  return

#Ejercicio2
def mayor():
  x = float(input("Digite un numero: "))
  y = float(input("Digite un numero: "))
  z = float(input("Digite un numero: "))

  if (x > y) and (x > z): 
   print("El numero mayor es:",x)
  elif (z > x) and (z > y):
   print("El numero mayor es:",z)
  elif (y > x) and (y > z):
   print("El numero mayor es:",y)
  elif (y == x) and (y == z) and (x == y) and (x == z) and (z == x) and (z == y):
   print("Todos los números son iguales") 
  return

#Ejercicio3
def impares():
 num = [1,2,3,4,5,6,7,8,9,10]
 simpares =0
 i=0
 while i <len(num):
    if num[i] % 2 != 0:
        simpares += num[i]
    i +=1    
 print("Suma de valores impares en el rango 1 a 10: ",simpares)
 return

#Ejercicio4
def caracteres():
 frase = 'Bienvenidos'

 print("valor original:",frase)
 print(len(frase))
 print('{:^30}'.format(frase))
 return

#Menú
ans=True
while ans:
    print ("""
    1.Defina una función en python que acepte el radio y devuelva el valor del area de un círculo de esas dimensiones.\n
    2.Defina una función en python que acepte 3 valores y devuelva solo el maximo de los tres.\n
    3.Dado una lista de enteros, defina una función en python que devuelva la suma de solo los valores impares de dicha lista.\n
    4.Desarrolle una función en python que acepte una variable string como primer parámetro y la cantidad 
    de caracteres de como segundo parámetro. La función debe retornar un nuevo string que consista en el
    string original y el número correcto de caracteres necesarios para que el string se salga centrado.
    No agregue caracteres al final del string.\n
    5.Salir.
    """)
    ans=input("¿Qué ejercicio le gustaría hacer? ") 
    if ans=="1": 
      print("\n Ejercicio 1")
      calculodearea() 
    elif ans=="2":
      print("\n Ejercicio 2")
      mayor()
    elif ans=="3":
      print("\n Ejercicio 3")
      impares()
    elif ans=="4":
      print("\n Ejercicio 4")
      caracteres()
    elif ans=="5":
      print("\n Hasta luego.")
      break
    elif ans !="":
      print("\n Valor no válido. Intente de nuevo") 