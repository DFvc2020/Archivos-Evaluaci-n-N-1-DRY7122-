import json

nombre = input("Ingrese su nombre: Diego ")
apellido = input("Ingrese su apellido: Vasquez ")

datos = {
    "Diego": nombre,
    "Vasquez": apellido
}

json_datos = json.dumps(datos)

print(json_datos)
