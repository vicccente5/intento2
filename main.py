#agenda 
contacto = []

def agregar_contacto(nombre, telefono):
    contacto.append({"nombre": nombre, "telefono": telefono})

def listar_contactos():
    print("/nlistado de contactos:")
    for c in contacto:
        print("Nombre:", c["nombre"], "Teléfono:", c["telefono"])


nombre = input("Ingrese el nombre del contacto: ")
telefono = input("Ingrese el teléfono del contacto: ")
agregar_contacto(nombre, telefono)
print("Contacto agregado:", contacto)


