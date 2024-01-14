"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""


name = input('Digite o seu nome: ');
age = input('Digite a sua idade: ');

if name and age:
  invertName = name[::-1]
  hasSpace = ' ' in name
  nameLenght = len(name)
  firstLetter = name[0:1:]
  lastLetter = name[-1]

  print(f'Seu nome é {name}')
  print(f'Seu nome invertido é {invertName}')
  print(f'Seu nome contém espaços: {hasSpace}')
  print(f'Seu nome tem {nameLenght} letras')
  print(f'A primeira letra do seu nome é {firstLetter}')
  print(f'A última letra do seu nome é {lastLetter}')
else:
  print('Desculpe, você deixou campos vazios.')