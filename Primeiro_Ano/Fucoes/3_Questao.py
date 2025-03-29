# (UFMG) Suponha-se que o número f(x) de funcionários
# necessários para distribuir, em um dia, contas de luz
# entre x por cento de moradores, numa determinada
# cidade, seja dado pela função f(x) = 300x/(150 -x)
# Se o número de funcionários necessários para distribuir, em um dia, as
# contas de luz foi 75, a porcentagem de moradores que as receberam é
# 
# A) 25      B) 30       C) 40    D) 45      E) 50

def f(x):
    return 300*x/(150 - x)

# Note que y = f(x), onde termos que resolver a equação 75 = f(x)

from sympy import*

x = Symbol('x')

# 75 = 300*x/(150 - x) >>> 0 = 300*x/(150 - x) - 75

eq = 300*x/(150 - x) - 75

solucao = solve(eq)

print(f'O valor de x = {max(solucao)}%')
print(f'Resposta B)')

# Note que f(30) = 75

print(f'\nValor de f(x), quando x = 30')
print(f'{f(30)}')