import xml.etree.ElementTree as ET

nombre = input("Ingrese su nombre:Diego ")
apellido = input("Ingrese su apellido:Vasquez ")

root = ET.Element("datos")
ET.SubElement(root, "nombre").text = nombre
ET.SubElement(root, "apellido").text = apellido

xml_tree = ET.ElementTree(root)
xml_tree.write("datos.xml")

