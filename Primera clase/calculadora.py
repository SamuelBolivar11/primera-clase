"""
5
5

suma:10
menos:0
multiplicacion:25
divicion:1

"""

print("Introduce el primer numero")
numero1 =float(input("> "))

print("Introduce el segundo numero")
numero2 =float(input("> "))

suma = numero1 + numero2

resta = numero1 - numero2

multipli = numero1 * numero2

divi = numero1 / numero2

if numero2 != 0:
    divi = numero1 / numero2
else:
    divi = "No existe"

print(f"""
      suma: {suma}
      resta: {resta}
      multiplicacion {multipli}
      division: {divi}
      """)