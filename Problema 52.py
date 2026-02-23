#Problema 52

productos = ["Producto A", "Producto B", "Producto C", "Producto D", "Producto E"]
precios = [150.50, 200.00, 350.75, 100.25, 500.00]
ventas = [50, 30, 25, 80, 15]
print("Reporte de productos:")
print("Nombre\t\tPrecio\t\tVolumen Ventas\t\tIngreso")
for nom, pre, ven in zip(productos, precios, ventas):
    ingreso = pre * ven
    print(f"{nom}\t\t{pre:.2f}\t\t{ven}\t\t\t{ingreso:.2f}")
