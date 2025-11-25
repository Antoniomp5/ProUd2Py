# Variables del producto
producto = "Expresso doble"

precio_uni = 3.50 # Precio por unidad

# Variables de la Transacción

cantidad = 3

iva = 1.16 #16% de IVA

# Variables del cliente

cliente_nombre = "Ana María López"

id_trasn = "CAF-2025-472" # id de trasncripción

# Cálculo del pedido y recibo
sub = precio_uni * cantidad
total = sub * iva

print(f"====Cafetería ._. | ID: {id_trasn}====")
print(" ")
print(f"Cliente: {cliente_nombre}")
print(f"Pedido: {producto} ({cantidad} unidades)")
print(f"Precio sin IVA: {sub}")
print(f"Precio total: {total}")
print(" ")
print(f"========Grácias por su visita==========")