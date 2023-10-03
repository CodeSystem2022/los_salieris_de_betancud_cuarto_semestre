# help(str.capitalize)

mensaje_1 = 'hola mundo'
mensaje_2 = mensaje_1.capitalize()
print('Mensaje 1:', mensaje_1, 'id:', id(mensaje_1))
print('Mensaje 2:', mensaje_2, 'id:', id(mensaje_2))

mensaje_1 += ', Adios'
print('Mensaje 1:', mensaje_1, 'id:', id(mensaje_1))