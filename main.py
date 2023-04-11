#Autor:Anderson Antonio de Melo
#Esse programa tem como finalidade efetuar o calculo do #IMC(Indice de Massa Corporal) de uma pessoa
#OBS: para o calculo do IMC temos que:
#IMC = peso/(altura*altura)

print('### Calculo de IMC(Indice de Massa Corporal ###')
nome = input('\nPor favor digite seu nome: ')
idade = int(input('Por favor digite sua idade: '))
peso = float(input('Por favor digite seu peso: '))
altura = float(input('Por favor digite sua altura: '))

imc = peso/(altura**2)#pode ser feito tbm desse jeito: peso/(altura*altura)

print('\n#### Segue os dados do(a) cliente ####')
print('\nCliente:',nome)
print('Idade do(a) cliente:',idade,'anos')
print('Peso do cliente:',peso,'kg')
print('Altura do(a) cliente:',altura,'metros')
print('Caro cliente',nome,'seu IMC e de:',imc)