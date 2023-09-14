from decimal import Decimal

a = float('NaN')
print(f'a: {a}')

#* Módulo 'math'
import math

print('Es tipo NaN: ', math.isnan(a))

a = Decimal('NaN')
print('Es tipo NaN: ', math.isnan(a))
