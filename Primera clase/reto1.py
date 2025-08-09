"""
Escribe un programa que pregunte al
usuario por el numero de horas trabajadas
y el costo por hora. Luego imprime en
pantalla el pago que le corresponde.
PAGO = HORAS * COSTO
"""

print("Digite la cantidad de horas trabajadas")
horas_trabjadas = int(input("> "))

print("Digame el costo por hora")
costo_hora = int(input("> "))

print(f"""
      Segun:
        Horas Trabajadas: {horas_trabjadas}
        Costo por hora: {costo_hora}
        Ganancia Total: {horas_trabjadas*costo_hora}
      """)

if costo_hora>10000:
    print("Eres millonario")
elif costo_hora >= 5000:
    print("vas a mitad de camino")
else:
    print("Tienes que chambear mas")