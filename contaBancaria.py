class ContaBancaria():

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False 

    def __str__(self):
        return f'Titular: {self._titular} | Saldo: {self._saldo}'
    
    
    def ativar_conta(self):
        self._ativo = True

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo
        
    @property
    def ativo(self):
        return f'A conta de {self._titular} está Ativa' if self._ativo else f'A conta de {self._titular} está Inativa'
   



conta1 = ContaBancaria('Renato', 1000)
conta2 = ContaBancaria('Yasmim', 2000)

conta1.ativar_conta()

print(conta1)
print(conta2)

print(conta1.ativo)
print(conta2.ativo)