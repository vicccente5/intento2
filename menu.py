#menu
from listas import *

while True:
        print("\nMenu de opciones:")
        print("1. Agregar contactos")
        print("2. listar contactos")
        print("3. Buscar contacto") 
        print("4. salir")

        opcion = input("Seleccione una opcion (1-4): ")
 
        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el teléfono del contacto: ")
            agregar_contacto(nombre, telefono)
            print("Contacto agregado exitosamente.")
        elif opcion == "2":
            listar_contactos()
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            buscar_contacto(nombre)
        elif opcion == "4":
            print("Saliendo del programa.")
            break#no puedo hacer que el breake termine el programa
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

        
