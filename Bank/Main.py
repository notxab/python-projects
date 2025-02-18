class main:
    pass

print('testando!')

from Cliente import Cliente
from Conta import Conta

c1=Cliente('Joao', "114444-2222")
conta=Conta(c1.nome,6565,0)

print(c1)
print(c1.nome,' e ',c1.telefone)

print(f'{conta.titular} Numero: {conta.numero} "Seu Saldo: {conta.saldo}')