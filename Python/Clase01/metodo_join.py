# help(str.join)

tupla_str = ('Hola', 'alumnos', 'Tecnicatura', 'Universitaria')
mensaje = ' '.join(tupla_str)
print('Mensaje:', mensaje)

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
print('Mensaje:', mensaje)

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print('Mensaje:', mensaje)

diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': '18'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print('Llaves:', llaves, 'Type:', type(llaves))
print('Valores:', valores, 'Type:', type(valores))
