# Exercício 13 – Reajuste Salarial

sal = float(input('Qual é o salário do funcionário? R$ '))
salnovo = sal + (15/100 * sal)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(sal,salnovo))
