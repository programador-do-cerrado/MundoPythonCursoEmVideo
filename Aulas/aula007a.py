n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale: {} '.format(s))
print('A multiplicação vale: {} '.format(m), end=', ')
print('A divisão vale: {:.3f}'.format(d), end=', ')
print('A divisão inteira vale: {}'.format(di),)
print('O primeiro termo elevado ao segundo termo vale: {}'.format(e))

"""
Pq eu deixei a linha 3 desse jeito???
pq eu só utilizei esse calculo naquele momento, 
não foi necessário criar uma variavel para isso. 
"""
