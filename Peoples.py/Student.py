#exercicio 01
student = dict()
student['nome'] = str(input('nome: '))
student['média'] = float(input(f'Média do {student["nome"]}: '))
if student['média'] >= 6: 
  student['estado'] = 'Aprovado'
elif 5 <= student['média'] < 6:
  student['estado'] = 'Recuperação'
else:
  student['estado'] = 'Reprovado'
print('-=' * 30)
for a, b in student.items():
  print(f' {a} {b}')
  