# Exercício 12 – Calculando Descontos

prod = float(input('Qual é o preço do produto? R$ '))
desc = (5/100)*prod
proddesc = prod - desc
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(prod,proddesc))
