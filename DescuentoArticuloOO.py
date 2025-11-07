valor = float(input("Ingrese el valor del producto: "))
tipo = float(input("Ingrese el tipo del producto: "))
if tipo == 1:
  descuento = valor*0.125
elif tipo == 2:
  descuento = valor*0.083
elif tipo == 3:
  descuento = valor*0.032
else:
  descuento = 0 

precioFinal = valor-descuento
print("Tu valor final seria: ",precioFinal)

