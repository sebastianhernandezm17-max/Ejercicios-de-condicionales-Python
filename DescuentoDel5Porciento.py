producto = float(input("Ingrese el valor del producto: "))
if producto > 150000:
 descuento = producto*0.05
 valorFinal = producto-descuento
 print("El valor de su producto es:",valorFinal)
else:
 print("El valor del producto es:",producto)
precioFinal = producto-descuento
print("Tu valor final seria: ",precioFinal)