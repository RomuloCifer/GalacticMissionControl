# Sistema Bancário

Um sistema bancário orientado a objetos implementado em Python que simula operações básicas de contas correntes e poupanças.

## 📋 Funcionalidades

- ✅ Gerenciamento de clientes e contas
- ✅ Dois tipos de conta: Corrente e Poupança
- ✅ Operações de depósito e saque
- ✅ Sistema de autenticação cliente-conta
- ✅ Limite de crédito para conta corrente
- ✅ Validações de segurança

## 🏗️ Estrutura do Sistema

### Classes Principais

#### `Pessoa`
Classe base que representa uma pessoa física.
- **Atributos**: nome, idade
- **Métodos**: getters para nome e idade

#### `Cliente`
Herda de `Pessoa` e representa um cliente do banco.
- **Atributos**: nome, idade, conta
- **Funcionalidade**: Vincula uma pessoa a uma conta bancária

#### `Conta` (ABC)
Classe abstrata que define o comportamento base de uma conta bancária.
- **Atributos**: agência, número, saldo
- **Métodos**: 
  - `depositar()`: Adiciona valor ao saldo
  - `sacar()`: Método abstrato a ser implementado pelas subclasses
  - Getter/Setter para saldo com validação

#### `ContaCorrente`
Implementação concreta de conta corrente com limite de crédito.
- **Funcionalidades**:
  - Saque até o limite do saldo + limite de crédito
  - Cobrança de juros quando utiliza o limite
  - Limite padrão de R$ 100

#### `ContaPoupanca`
Implementação concreta de conta poupança.
- **Funcionalidades**:
  - Saque apenas até o valor do saldo disponível
  - Sem limite de crédito

#### `Banco`
Classe que gerencia clientes e contas.
- **Funcionalidades**:
  - Armazena listas de clientes e contas
  - Sistema de autenticação cliente-conta

## 🚀 Como Usar

### Exemplo Básico

```python
from sistema_bancario import *

# Criar contas
conta_corrente = ContaCorrente("0001", "12345", limite=500)
conta_poupanca = ContaPoupanca("0001", "67890")

# Criar cliente
cliente = Cliente("João Silva", 30, conta_corrente)

# Criar banco e adicionar cliente/conta
banco = Banco()
banco.clientes.append(cliente)
banco.contas.append(conta_corrente)

# Operações bancárias
conta_corrente.depositar(1000)
conta_corrente.sacar(150)

# Autenticação
if banco.autenticar(cliente, conta_corrente):
    print("Cliente autenticado com sucesso!")
```

### Operações Disponíveis

#### Depósito
```python
conta.depositar(500)  # Deposita R$ 500
```

#### Saque - Conta Corrente
```python
conta_corrente.sacar(1200)  # Pode usar limite se necessário
```

#### Saque - Conta Poupança
```python
conta_poupanca.sacar(800)  # Apenas se houver saldo suficiente
```

## 🔒 Validações e Segurança

- **Saldo**: Não pode ser negativo
- **Depósito**: Apenas valores positivos
- **Saque**: Validação de saldo disponível
- **Autenticação**: Verificação cliente-conta no banco

## 🏛️ Arquitetura

O sistema utiliza conceitos de programação orientada a objetos:

- **Herança**: `Cliente` herda de `Pessoa`
- **Abstração**: `Conta` como classe abstrata
- **Encapsulamento**: Atributos privados com getters/setters
- **Polimorfismo**: Diferentes implementações de `sacar()`

## 📁 Estrutura de Arquivos

```
sistema_bancario.py    # Código principal
README.md             # Documentação
```

## 🔧 Requisitos

- Python 3.6+
- Módulo `abc` (já incluído no Python)

## 📝 Melhorias Futuras

- [ ] Histórico de transações
- [ ] Taxas e tarifas
- [ ] Diferentes tipos de conta poupança
- [ ] Sistema de notificações
- [ ] Interface gráfica
- [ ] Persistência de dados
- [ ] Relatórios bancários

## 👨‍💻 Autor

Sistema desenvolvido como exemplo de programação orientada a objetos em Python.

---

**Nota**: Este é um sistema educacional para demonstração de conceitos de POO. Não deve ser usado em ambiente de produção sem as devidas implementações de segurança.
