# Em uma Locadora de Carros, o preço do aluguel custa R$ 60,00 por dia  
# e cobra R$ 0,15 por quilometros rodados. Um cliente dessa locadora, 
# percorreu 500km durante 10 dias. 
# Qual é o valor que esse cliente vai ter que pagar para a Locadora?

Km_percorrido = 500

dias_alugado = 10

valor_aluguel = 60 # Aluguel do Carro

km_rodado = 0.15 # preço cobrado por Km rodados

preco_a_pagar = dias_alugado*valor_aluguel + Km_percorrido*km_rodado

print(f'O preço a pagar é: {preco_a_pagar}')