nota1 = float(input("Ingresa su primera nota: ")) 
nota2 = float(input("Ingresa su segunda nota: ")) 
nota3 = float(input("Ingresa su tercera nota: ")) 
nota4 = float(input("Ingresa su cuarta nota: ")) 
nota5 = float(input("Ingresa su quinta nota: ")) 

notaFinal = (nota1+nota2+nota3+nota4+nota5)/5
if notaFinal >= 3.5:
  print("Ganaste el curso")
  print("Su nota final es:",notaFinal)
else:
  print("Perdiste el curso")
  print("Su nota final es:",notaFinal)