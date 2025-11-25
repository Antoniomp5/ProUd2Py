import re

data = """
Usuario: perez.juan
Email de contacto: juan.perez@dominio.com
Fecha de acceso: 15-09-2023
Código de cliente: ABC123456
Teléfono de emergencia: 601 234 567
Archivos encontrados: a_1.txt, b_22.py, c_333.pdf, d_4444.jpg
"""
#A
p1 = r'\w+\.\w+@\w+\.\w{3}'
print(re.findall(p1, data))
#B
p2 = r'\d{2}-\d{2}-\d{4}'
print(re.findall(p2, data))
#C
p3 = r'\w\w\w+\d{6}'
print(re.findall(p3, data))
#D
p4 = r'\w+\.+\w*py'
print(re.findall(p4, data))