import yaml

nombre = input("Ingrese su nombre:Diego ")
apellido = input("Ingrese su apellido:Vasquez ")

datos = {"Diego": nombre, "Vasquez": apellido}

print("Datos en formato YAML:")
print(yaml.dump(datos))
