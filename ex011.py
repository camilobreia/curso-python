# Exercício 11 – Pintando Parede

l = float(input('Largura da parede (em metros): '))
a = float(input('Altura da parede (em metros): '))
mq = l * a
t = mq / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m². \nPara pintar essa parede, você precisará de {}l de tinta'.format(l,a,mq,t))
