fils = int(input("Cuantas filas?: "))
cols = int(input("Cuantas columnas?: "))

lstPrecios = []
print(f"Ingrese el precio para cada uno de los {fils} productos:")
for f in range(fils):
    precio = int(input(f"Precio del producto {f}: "))
    lstPrecios.append(precio)

matVentas = []
print(f"\nIngrese las unidades vendidas por día ({cols} días) para cada producto:")
for f in range(fils):
    print(f"--- Producto {f} ---")
    fila_ventas = []
    for c in range(cols):
        venta = int(input(f"  Día {c + 1}: "))
        fila_ventas.append(venta)
    matVentas.append(fila_ventas)

def lstTotalesProdxSem(ventas, precios):
    lstTotales = []
    for f in range(len(ventas)):
        suma = 0
        for c in range(len(ventas[0])):
            suma += ventas[f][c] * precios[f]
        lstTotales.append(suma)
    return lstTotales

lstTotales = lstTotalesProdxSem(matVentas, lstPrecios)
maxTotal = max(lstTotales)
prodVentMax = lstTotales.index(maxTotal)

print("\n----------------------------------------")
print(f"El producto {prodVentMax} es el que mas vende a la semana con ventas de: ${maxTotal:,}")

def diaMayorVenta(ventas, precios):
    ventasPorDia = [0] * cols
    for c in range(cols):
        total_dia = 0
        for f in range(fils):
            total_dia += ventas[f][c] * precios[f]
        ventasPorDia[c] = total_dia
    return ventasPorDia

lstVentasDia = diaMayorVenta(matVentas, lstPrecios)
maxVentaDia = max(lstVentasDia)
diaMax = lstVentasDia.index(maxVentaDia)

print(f"El dia {diaMax + 1} fue el de mayores ventas totales con un valor de: ${maxVentaDia:,}")