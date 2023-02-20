#exercicio 03
from datetime import datetime
infos = dict()
infos['nome '] = str(input('nome:'))
nascdate = int(input('Ano de Nascimento: '))
infos['idade'] = datetime.now().year - nascdate
infos['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if infos['ctps '] != 0:
  infos['salário'] = float(input('Salário: R$ '))
  infos['contratação'] = int(input('Ano de Contratação '))
  infos['aposentadoria'] = infos['idade'] + ((infos['contratação'] + 35) - datetime.now().year)
print ('-=' * 30)
for a1, a2 in infos.items():
  print(f' - {a1} {a2}')
