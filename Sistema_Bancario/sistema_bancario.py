from abc import ABC,abstractmethod
class Pessoa():
    def __init__(self,nome,idade):
        self._nome = nome
        self._idade = idade
    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        return self._idade
    
class Cliente(Pessoa):
    def __init__(self,nome,idade,conta):
        super().__init__(nome,idade)
        self.conta = conta
    
class Conta(ABC):
    def __init__(self,agencia,numero):
        self.agencia = agencia
        self.numero = numero
        self._saldo = 0
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self,valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print("saldo não pode ser negativo.")

    def depositar(self,valor):
        valor = int(valor)
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor inválido para depósito.")

    @abstractmethod
    def sacar(self):
        ...

class ContaCorrente(Conta):
    def __init__(self,agencia,numero,limite = 100):
        super.__init__(agencia,numero)
        self.limite = limite

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Novo saldo R${self.saldo}")
        elif valor > self.saldo:
            if valor <= (self.saldo + self.limite):
                self.limite -=  valor - self.saldo
                self.saldo = 0                
                print(f"Novo saldo R${self.saldo}, R${self.limite} de juros")
            else:
                print(f"Valor não disponível para saque.")

class ContaPoupanca(Conta):
    def __init__(self,agencia,numero,):
        super.__init__(agencia,numero)    
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Novo saldo R${self.saldo}")
        else:
            print(f"Valor não disponível para saque.")     

class Banco():
    def __init__(self,contas= None,clientes = None):
        self.contas = contas if contas else []
        self.clientes = clientes if clientes else []

    def autenticar(self,cliente,conta):
        if (
            cliente in self.clientes and
            conta in self.contas and
            cliente.conta == conta
        ):
            return cliente in self.clientes and conta in self.contas and cliente.conta == conta
        else:
            return False


