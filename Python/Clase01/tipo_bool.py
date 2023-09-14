
#* con números
valor = 0
resultado = bool(valor)
print(f'valor (número): {valor} -> resultado: {resultado}')

valor = 0.1
resultado = bool(valor)
print(f'valor (número): {valor} -> resultado: {resultado}')

#* con cadenas
valor = ''
resultado = bool(valor)
print(f'valor (cadena): {valor} -> resultado: {resultado}')

valor = 'algo'
resultado = bool(valor)
print(f'valor (cadena): {valor} -> resultado: {resultado}')

#* con listas
valor = []
resultado = bool(valor)
print(f'valor (lista): {valor} -> resultado: {resultado}')

valor = ['algo']
resultado = bool(valor)
print(f'valor (lista): {valor} -> resultado: {resultado}')

#* con tuplas
valor = ()
resultado = bool(valor)
print(f'valor (tupla): {valor} -> resultado: {resultado}')

valor = ('algo', )
resultado = bool(valor)
print(f'valor (tupla): {valor} -> resultado: {resultado}')

#* con diccionarios
valor = {}
resultado = bool(valor)
print(f'valor (diccionario): {valor} -> resultado: {resultado}')

valor = {1: 'algo'}
resultado = bool(valor)
print(f'valor (diccionario): {valor} -> resultado: {resultado}')

#* en sentencias de control
if ('algo', ):
    print('Regresa verdadero')
else:
    print('Regresa falso')

#* en ciclos
variable = 17
while variable:
    print('regresa verdadero')
    break
else:
    print('regresa falso')