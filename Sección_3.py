import re

def lexer(codigo):
    tokens = []

    patrones = [
        (r'\bif\b', 'IF'),
        (r'\belse\b', 'ELSE'),
        (r'\bwhile\b', 'WHILE'),
        (r'\d+\.\d+', 'NUMERO_DECIMAL'),
        (r'\d+', 'NUMERO_ENTERO'),
        (r'[a-zA-Z_]\w*', 'IDENTIFICADOR'),
        (r'\+', 'SUMA'),
        (r'-', 'RESTA'),
        (r'\*', 'MULTIPLICACION'),
        (r'/', 'DIVISION'),
        (r'>', 'MAYOR_QUE'),
        # Puedes agregar más como (, ), :, etc. si lo necesitas
    ]

    # Eliminar comentarios y espacios
    codigo = re.sub(r'#.*', '', codigo)
    codigo = codigo.strip()

    for patron, tipo in patrones:
        for match in re.finditer(patron, codigo):
            tokens.append((tipo, match.group()))

    return tokens

# Ejemplo de uso (como en el examen)
codigo_prueba = "if x >15: y = 3.14 * x # calculo"
print(lexer(codigo_prueba))
