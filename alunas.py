nome= input('Digite o nome da anula: ')
idade= int(input('Digite a idade da aluna: '))
altura= float(input('Digite a altura da aluna: '))
hobbies= input('Digite os hobbies das alunas separados por virgulas: ')
hobbies1= hobbies.split (',') # transforma os hobbies em uma lista
endereco_rua= input('Digite o nome da rua da aluna: ')
endereco_numero= int(input('Digite o número da casa da aluna: '))
endereco_cidade= input ('Digite a cidade da aluna: ')
endereco= (endereco_rua,endereco_numero,endereco_cidade)
email= input('Digite o e-mail da aluna: ')
telefone= input('Digite o telefone da aluna: ')
contato= {'email':email, 'telefone': telefone} #cria um dicionário

print( '\nOlá, segue informaçao sobre a aluna: ') #\n pula uma linha
print('Nome:', nome)
print('Idade:', idade)
print('altura:', altura)
print('Hobbies:', hobbies1)
print('Endereço:', endereco)
print('Contato:', contato)