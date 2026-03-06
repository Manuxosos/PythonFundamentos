nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = nota1 + nota2 + nota3
numero = promedio/3
if numero >= 1 and numero <= 3:
    print("Mejorarable", numero)
elif numero == 0:
    print("Reprobado")
elif numero >= 3 and numero  < 6 :
    print("Bueno", numero)
elif numero >= 6 and numero < 8:
    print("excelente", numero)
elif numero >=8  and  numero <= 10:
    print("sobresaliente", numero)
else:
    print("Error" , numero)
