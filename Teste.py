cpf = input('Informe o CPF: ')
nome = input('Informe o Nome: ')
endereco = input('Informe o Endereço: ')
print('CPF:', cpf, '\nNome:', nome, '\nEnd.:', endereco)

x =  [1,'hello',10]
for i in range(len(x)):
  print(x[i])

def intersecao(conjuntoA, conjuntoB):
    inter = [x for x in range(1,90) if x in conjuntoA and conjuntoB]
    return inter

a = [1,1,2,3,5,8,13,21,34,55,89]
b =  [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(intersecao(a,b))
