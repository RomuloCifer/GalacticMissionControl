# 🚀 Galactic Mission Control

Sistema de controle de missões espaciais com monitoramento e validação automática.

## ✨ Características

- 🛡️ **Segurança**: Bloqueia ações de autodestruição automaticamente
- 📊 **Logs**: Registro automático de todas as ações executadas
- 🔤 **Normalização**: Suporte a acentos e caracteres especiais
- ✅ **Validação**: Verificação robusta de tipos de dados

## 🚀 Uso Rápido

```python
from GalacticMissionControl import *

# Criar planeta, equipe e missão
marte = Planeta("Marte", 227_900_000, "Planeta vermelho")
equipe = Equipe("Alpha", ["João", "Maria"])
missao = Missao(1, marte, equipe)

# Executar ação
resultado = missao.executar("explorar superfície")
print(resultado)
```

## 📚 Classes Principais

### Planeta
```python
planeta = Planeta(nome, distancia_km, descricao)
print(planeta.distancia)  # Em UA
print(planeta.descricao_completa())
```

### Equipe
```python
equipe = Equipe("Nome", ["membro1", "membro2"])
equipe.adicionar_membro("novo_membro")
equipe.remover_membro("membro1")
print(len(equipe))  # Número de membros
```

### Missao
```python
missao = Missao(numero, planeta, equipe)
missao.executar("ação")  # Executa com monitoramento
missao.cancelar()        # Cancela se não estiver executando
print(missao.status)     # "criada", "executando", "concluída", "cancelada"
```

## 🔧 Funções Úteis

```python
# Listar e filtrar missões
listar_missoes()                          # Lista todas
obter_missao(numero)                      # Busca por número
listar_missoes_por_status("concluída")    # Filtra por status
estatisticas_missoes()                    # Mostra estatísticas
```

## ⚠️ Sistema de Segurança

```python
# Estas ações são BLOQUEADAS automaticamente:
missao.executar("autodestruição")     # RuntimeError
missao.executar("AUTODESTRUICAO")     # RuntimeError (normalizado)

# Alertas automáticos:
missao.executar("situação crítica")   # Mostra "⚠ Sistema em risco"
```

## 📋 Logs Automáticos

```python
# Verificar histórico de ações
for timestamp, acao in log_global.items():
    print(f"{timestamp}: {acao}")
```

## 🛠️ Instalação

1. Baixe `GalacticMissionControl.py`
2. Importe: `from GalacticMissionControl import *`
3. Requer Python 3.6+

---
**Missões espaciais seguras e monitoradas! 🌌**