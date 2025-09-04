#agenda 
contacto = []

def agregar_contacto(nombre, telefono):
    contacto.append({"nombre": nombre, "telefono": telefono})

def listar_contactos():
    print("\nlistado de contactos:")
    for c in contacto:
        print("Nombre:", c["nombre"], "Teléfono:", c["telefono"])

def buscar_contacto(nombre):
    for c in contacto:
        if c["nombre"].lower() == nombre.lower():
            print(f"Contacto encontrado: Nombre: {c['nombre']}, Teléfono: {c['telefono']}")
            return 
        print("Contacto no encontrado.")


