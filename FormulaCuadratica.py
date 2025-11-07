a= float(input("Ingrese el valor de a: ")) 
b= float(input("Ingrese el valor de b: ")) 
c= float(input("Ingrese el valor de c: ")) 
d = b**2-4*a*c
if b**2-4*a*c >= 0:
  print("Tiene solucion")
  print("El valor dentro de la raiz cuadrada es:",d)
else:
  print("No tiene solucion")
  print("El valor dentro de la raiz cuadrada es:",d)