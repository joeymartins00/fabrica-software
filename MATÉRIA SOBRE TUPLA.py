alunos = ['Alessandra','Joceyr','Thiago','Vitor']
print(alunos)
print(alunos[0])
print(alunos[3])
print(alunos[1])
print(alunos[2])
for al in range(0,len(alunos)):
    print(f'Os alunos da Fábrica são {alunos}')
print('*'*50)

for al in range(0,len(alunos)):
    print(f'Os alunos da Fábrica são {al}')
print('*'*50)

for al in range(0,len(alunos)):
    print(f'Os alunos da Fábrica são {alunos[al]}')
print('*'*50)

for al in range(0,len(alunos)):
    print(f'Os alunos da Fábrica são {alunos[al]} e estão na posição {al} da tupla')
print('*'*50)

print('De trás pra frente')

for al in range(-1, -5, -1):
    print(f'Os alunos da Fábrica são {alunos[al]}')
print('*'*50)