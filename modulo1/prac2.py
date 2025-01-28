# PRACTICA NRO 2
#  DEFINA EL SIGUIENTE DICCIONARIO
ventas=[
    {
        "fecha":"12-01-2023",
        "producto":"Producto_A",
        "cantidad":50,
        "precio":45.00,
        "promocion":True
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_AX",
        "cantidad":160,
        "precio":12.00,
        "promocion":False
    },
    {
        "fecha":"10-01-2023",
        "producto":"Producto_D",
        "cantidad":20,
        "precio":15.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_C",
        "cantidad":10,
        "precio":140.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_D",
        "cantidad":1200,
        "precio":1.00,
        "promocion":True
    }
]

# 1. CREA UN MENU ITERACTIVO QUE CUENTE CON LOS SIGUIENTES OPCIONES
# 2. Mostrar el listado de ventas => puedes usar print(f"")
# 3. Añadir un producto
# 4. Calcular la suma total de las ventas
# 5. Calcular el promedio de ventas
# 6. Mostar el producto mas unidades vendidas
# 7. Mostrar el listado de productos

def mostrar_ventas():
    print("Listado de Ventas:")
    for venta in ventas:
        print(f"Fecha: {venta['fecha']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Promoción: {venta['promocion']}")

def anadir_producto():
    print("Añadir un producto:")
    fecha = input("Ingrese la fecha: ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    while True:
        promocion_input = input("¿Está en promoción? (True/False): ")
        if promocion_input in ["True", "False"]:
            promocion = promocion_input == "True"
            break
        else:
            print("Entrada no válida. Por favor, ingrese 'True' o 'False'.")
    nueva_venta = {
        "fecha": fecha,
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio,
        "promocion": promocion
    }
    ventas.append(nueva_venta)
    print("Producto añadido correctamente.")

def suma_total_ventas():
    total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    print(f"La suma total de las ventas es: {total}")

def promedio_ventas():
    total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    promedio = total / len(ventas) if ventas else 0
    print(f"El promedio de las ventas es: {promedio}")

def producto_mas_vendido():
    producto_max = max(ventas, key=lambda venta: venta['cantidad'])
    print(f"El producto con más unidades vendidas es: {producto_max['producto']} ({producto_max['cantidad']} unidades)")

def mostrar_listado_productos():
    productos = {venta['producto'] for venta in ventas}
    print("Listado de productos:")
    for producto in productos:
        print(producto)

while True:
    print(
    """
    Bienvenido al Menú interactivo"""
    )
    print("""
    1.Listado de ventas
    2.Añadir producto
    3.Suma total de ventas
    4.Promedio de ventas
    5.Producto mas unidades vendidas
    6.Listado de productos
    """
    )

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
            mostrar_ventas()
    elif opcion == "2":
            anadir_producto()
    elif opcion == "3":
            suma_total_ventas()
    elif opcion == "4":
            promedio_ventas()
    elif opcion == "5":
            producto_mas_vendido()
    elif opcion == "6":
            mostrar_listado_productos()
    elif opcion == "7":
            print("Saliendo del programa.")
            break
    else:
            print("Opción no válida, por favor intente de nuevo.")
            