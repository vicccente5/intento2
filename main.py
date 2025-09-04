#agenda 
contacto = ()

def agregar_contacto(nombre, telefono):
    contacto.append({"nombre": nombre, "telefono": telefono})

nombre = input("Ingrese el nombre del contacto: ")
telefono = input("Ingrese el teléfono del contacto: ")
agregar_contacto(nombre, telefono)
print("Contacto agregado:", contacto)
