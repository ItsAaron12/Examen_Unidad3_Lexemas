import re  # Importamos el módulo para trabajar con expresiones regulares

# -------------------------
# FUNCIONES
# -------------------------

# (Opcional) Esta función iba a usarse para análisis léxico pero está vacía
# Se ha preparado para eliminar comentarios y espacios
def lexer(codigo):
    # Eliminar todo lo que esté después de un '#' (comentarios)
    codigo = re.sub(r'#.*', '', codigo)

    # Eliminar espacios iniciales y finales del código
    codigo = codigo.strip()
    
    # La función actualmente no devuelve nada, puede completarse si se desea usar
    return []  # Para evitar error de "NoneType", retornamos una lista vacía

# -------------------------
# SECCIÓN 4 - EXPRESIONES REGULARES
# -------------------------

# Función que extrae correos electrónicos de un texto usando regex
def extraer_emails(texto):
    # Patrón que detecta emails válidos como usuario@dominio.com
    patron_email = r'\b[\w.-]+@[\w.-]+\.\w+\b'
    return re.findall(patron_email, texto)

# Función que extrae horas en formato 24h (HH:MM) válidas
def extraer_horas(texto):
    # Patrón que detecta horas desde 00:00 hasta 23:59
    patron_hora = r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b'
    return re.findall(patron_hora, texto)

# -------------------------
# PRUEBAS DE FUNCIONALIDAD
# -------------------------

# Prueba del lexer (aunque no realiza tokenización aún)
codigo_prueba = "if x >15: y = 3.14 * x # calculo"
print("📌 Tokens encontrados:")
print(lexer(codigo_prueba))  # Retorna lista vacía por ahora

# Prueba para extraer emails de un texto dado
texto_emails = "Contactos: ana@example.com , bob@mail.org; soporte@empresa.com"
print("\n📧 Correos encontrados:")
print(extraer_emails(texto_emails))  # Debería mostrar una lista con 3 emails

# Prueba para extraer horas válidas de un texto
texto_horas = "Reuniones: 09:30, 14:00 y 23:59. Hora incorrecta: 25:00"
print("\n🕒 Horas encontradas:")
# Los resultados se muestran como listas de tuplas, así que se unen con ':'
print([':'.join(hora) for hora in extraer_horas(texto_horas)])
