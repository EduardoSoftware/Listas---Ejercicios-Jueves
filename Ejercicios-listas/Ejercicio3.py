def main():
    inventario = []
    
    while True:
        print("\nMENÚ")
        print("1. Agregar producto")
        print("2. Agregar lote de productos")
        print("3. Eliminar producto del inventario")
        print("4. Eliminar el producto más reciente")
        print("5. Ordenar productos alfabéticamente")
        print("6. Mostrar número total de productos")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            inventario.append(nombre)
            print("Producto agregado con éxito.")
            
        elif opcion == "2":
            cantidad = int(input("¿Cuántos productos desea agregar en el lote?: "))
            for _ in range(cantidad):
                nombre = input("Ingrese el nombre del producto: ")
                inventario.append(nombre)
            print("Lote agregado con éxito.")
            
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            if nombre in inventario:
                inventario.remove(nombre)
                print("Producto eliminado con éxito.")
            else:
                print("El producto no se encuentra en el inventario.")
                
        elif opcion == "4":
            if len(inventario) > 0:
                eliminado = inventario.pop()
                print(f"Producto más reciente eliminado: {eliminado}")
            else:
                print("El inventario está vacío.")
                
        elif opcion == "5":
            inventario.sort()
            print("Inventario ordenado alfabéticamente:")
            for p in inventario:
                print(f"- {p}")
                
        elif opcion == "6":
            print(f"Número total de productos en el inventario: {len(inventario)}")
            
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()