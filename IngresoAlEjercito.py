sexo = str(input("Ingrese su sexo (hombre/mujer)")) 
edad = str(input("Ingrese su edad")) 
estadoCivil = str(input("Ingrese su estado civil (soltero/casado/divorciado/viudo)")) 
estatura = str(input("Ingrese su estatura")) 
sexo = sexo.lower()
estadoCivil = estadoCivil.lower()
if sexo == "mujer" and estadoCivil == "soltero" and estatura >= "1.60" and edad >= "20" and edad <= "25":
    print("Es apta") 
else:
    print("No es apta")  
if sexo == "hombre" and estadoCivil == "soltero" and estatura >= "1.65" and edad >= "18" and edad <= "24":
    print("Es apto")
else:
    print("No es apto")
