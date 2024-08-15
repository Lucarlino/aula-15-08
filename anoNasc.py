#declaração de variáveis 
nome = ""
anoNasc = anoAtual = idade = 0

#coletando os dados do usuário com a função input
nome = input('informe o seu nome: ')
anoNasc = int(input("informe seu ano de nascimento:"))
anoAtual = int(input("informe o ano atual:"))

idade = anoAtual - anoNasc

print('O usuário(a) ', nome, ' tem ', idade, ' anos .')