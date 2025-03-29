# (Enem–2010) Um laticínio possui dois reservatórios de leite.
# Cada reservatório é abastecido por uma torneira acoplada a
# um tanque resfriado. O volume, em litros, desses reservatórios
# depende da quantidade inicial de leite no reservatório e do
# tempo t, em horas, em que as duas torneiras ficam abertas.
# Os volumes dos reservatórios são dados pelas funções

# V1(t) = 250t³ – 100t + 3000 e V2(t) = 150t³ + 69t + 3000.

# Depois de aberta cada torneira, o volume de leite de
# um reservatório é igual ao do outro no instante t = 0 e,
# também, no tempo t igual a

# A) 1,3 h.       B) 1,69 h.          C) 10,0 h 
# D) 13,0 h       E) 16,9 h.

# Verificando os volumes dos resevatorios pelas funções
# em t = 0

def V1(t):
    return 250*t**3 - 100*t + 3000

def V2(t):
    return 150*t**3 + 69*t + 3000

print(f'Qundo t = 0, V1(0) = {V1(0)} =  V2(0) = {V2(0)}')

from sympy import*

t = Symbol('t')

# Fazendo V1 = 0 e V2 = 0, teremos duas equeções

eq1 = 250*t**3 - 100*t + 3000

eq2 = 150*t**3 + 69*t + 3000

# Onde teremos que achar o valor de t

eq3 = eq1 - eq2

solucao = solve(eq3) # Resolvendo a equação

print(f'\nValores de t são dados pelo conjunto solução S = {solucao}')

print(f'\nQueremos o valor positivo {max(solucao)}') # max retorna o maior valor de um número

print(f'\nA resposta correta é a letra A) {13/10}')

# Note que V1(13/10) e V1(13/10) é

print(F'\nValores de V1(t) e V2(t), em t = 13/10 é:')
print(f'{V1(13/10)} = {V2(13/10)}')