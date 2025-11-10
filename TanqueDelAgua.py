agua = float(input("Cuanta cantidad tiene su tanque de agua: ")) 
if agua < 250:
  print("Debe abrir la llave")
elif agua > 450:
    print("Debe cerrar la llave")
else:
   print("El tanque esta con la cantidad de adecuada")