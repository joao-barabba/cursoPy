frase = 'Olá mundão'
len(frase)# contar quantos elementos tem na lista
type(frase)# mostra o tipo de dado que esta variavael armazena
frase.replace('mundão','mundo')#função para fazer a substituição de dados
print(len(frase))
print(type(frase))
print(frase.replace('mundão','mundo'))
##Exemplos
cpf = 'CPF:46675470817'# Imagine ter acesso a uma base de dados desorganizada
int(cpf.replace('CPF:',''))#Usando este metodo consigo manipular a String
print(int(cpf.replace('CPF:','')))#Assim já deixando ela em Int para que eu possa vizualizar só o necessário.
#####
print(frase.startswith("Olá"))#Verifica o começo da string
print(frase.endswith("Olá"))#Verifica o final da string
#####
print(frase.count("O"))#Conta a quantidade de O na frase
#####
nome ="joao"# Definir o nome com letra minuscula    
nome = nome.capitalize()#utilizando o metodo Captalize e le transforma o j em J
print(nome)
#####
print(cpf.isdigit())#Este metodo verifica se a string é de apenas número e retorna True ou False
print(cpf.isalnum())# Verifica se a string é alfa númerica
#####
print(frase.find('Olá'))#Procura na String a posição onde começa aquilo que buscamos
#####
#strip()#Este metodo retira espaços no começo ou final das frases
#split(',') Ele quebra nossa string em fatias de acordo com o que queremos, neste caso a virgula foi usada como parametro