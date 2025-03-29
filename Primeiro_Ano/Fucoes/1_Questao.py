# (Enem–2010) Um dos grandes problemas da poluição dos
# mananciais (rios, córregos e outros) ocorre pelo hábito de
# jogar óleo utilizado em frituras nos encanamentos que estão
# interligados com o sistema de esgoto. Se isso ocorrer,
# cada 10 litros de óleo poderão contaminar 10 milhões
# (10⁷) de litros de água potável.

# Manual de etiqueta. Parte integrante das revistas Veja
# (ed. 2 055), Claudia (ed. 555), National Geographic (ed. 93)
# e Nova Escola (ed. 208) (Adaptação).

# Suponha que todas as famílias de uma cidade descartem
# os óleos de frituras através dos encanamentos e
# consomem 1^000 litros de óleo em frituras por semana.
# Qual seria, em litros, a quantidade de água potável
# contaminada por semana nessa cidade?

# A) 10²				C) 10⁴				E) 10⁹
# B) 10³				D) 10⁵


# 1º Forma de Resolver (Resolvendo por propriedade de potência)

# Note que a cada 10 litros de oléo contaminam 10⁷ litros de água 
# assim 10 >>> 10⁷

litros_de_oleo = int(input('Quantidade litros de óleo: '))

contaminacao_por_litros = 10**6 # pois 10/10 >>> 10⁷/10 = 1 >>> 10⁶ ou seja 
# a cada 1 litro de oléo contamina 10⁶ litros de água

agua_contaminada = litros_de_oleo*contaminacao_por_litros

print(f'Água contaminda por litro = {agua_contaminada:.1e} = {agua_contaminada}')

# Formatação para número cientfico agua_contaminada:.1e = 1.0e+07 = 10⁷

consumo_semanal = int(input('Quantidade semanal de litros de óleo consumido: '))

contaminacao_semanal = consumo_semanal*contaminacao_por_litros


print(f'\nA quantidade de água potável contaminada será de {contaminacao_semanal:.1e} = {contaminacao_semanal}')

print(f'A respota é a letra E)')

# 2º Forma de Resolver 

# Definir uma função

def f(x):
    return 10**6*x    # onde f(10) = 10⁷*10 = 10⁷

a = f(1000)

print(f'\nÁgua contaminada por semana: {a:.1e} = {a}')