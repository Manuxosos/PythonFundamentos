frutas = []
cantidad = int(input(" Cuantas frutas quieres agregar? "))
for i in range(cantidad):
    fruta = input(f"Escribe el nombre de la fruta {i+1}: ")
    frutas.append(fruta)
print("Lista de frutas ingresadas: ")
for f in frutas:
    print("-", f)