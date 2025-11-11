tareas_dia = ["Revisar Email", "Llamar al cliente", "comprar café", "Actualizar reporte", "Planificar reunión"]

tareas_orden = sorted(tareas_dia, key=str.lower)
# Quitar la almohadilla para descomentarlo
# tareas_dia.sort(key=len) 

print(tareas_orden)

print(tareas_dia)
