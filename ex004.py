thing = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(thing))
print('Só tem espaços? ', thing.isspace())
print('É um número? ', thing.isnumeric())
print('É alfabético? ', thing.isalpha())
print('É alganumérico? ', thing.isalnum())
print('Está em maiúsculas? ', thing.isupper())
print('Está em minúsculas? ', thing.islower())
print('Está capitalizada? ', thing.istitle())  # se a palavra está em maiúscula e minúscula
