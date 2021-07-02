from sunc import NotionClient
"""
# Nosso campo de formulas permitem esses 4 tipos de valores
float_number = 10.99999
integer = 10980
string = 'string'
booleano = False
booleano_verdadeiro = True
vazio = None

# Quero fazer implementar esses outros 2 para que o usuário consiga fazer mais coisas
lista_ou_array = [string, float_number, integer]
dicionario = {
    'chave': string
}


# não é um tipo primitivo (não é um valor)
def soma_com_retorno(a, b):
    return a+b

# As nossas formulas não precisam de retorno
def soma_sem_retorno(a,b):
    a+b


print('Soma com retorno: ' + str(soma_com_retorno(1, 2)))
print('Soma sem retorno: ' + str(soma_sem_retorno(1, 2)))
# uma variável pode ser uma formula para ser usada posteriormente
variavel_que_eh_formula = soma_com_retorno

variavel_que_eh_formula(float_number, integer)
"""

# Conceitos abstratos
#ass Notion:



client = NotionClient('secret_KkvznlgdwRX9tTItyvX83VtWOp4jp6LiSQV0W5pBYfO')
print(client.users.list_all().json['results'][0]['name'])