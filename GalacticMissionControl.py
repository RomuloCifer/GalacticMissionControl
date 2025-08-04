import datetime
import unicodedata
from functools import wraps


log_global = {}
registro_missoes = {}


def normalizar_texto(texto):

    if not isinstance(texto, str):
        return texto

    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sem_acentos = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    return texto_sem_acentos.lower()


def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f"{class_name} ({class_dict})"
    return class_repr


def add_repr(cls):
    cls.__repr__ = meu_repr
    return cls


@add_repr
class Planeta:
    def __init__(self, nome, distancia, descricao):
        self.nome = validar_entrada(nome, str, "nome")
        self._distancia_km = validar_entrada(distancia, (int, float), "distancia")
        self.descricao = validar_entrada(descricao, str, "descricao")

    @property
    def distancia(self):
        return self._distancia_km / 149_597_870.7

    def descricao_completa(self):
        return f"Planeta {self.nome} - {self.distancia:.2f} UA"


@add_repr
class Equipe:
    def __init__(self, nome, membros):
        self.nome = validar_entrada(nome, str, "nome")
        self.membros = validar_entrada(membros, list, "membros")
        if not self.membros:
            raise ValueError("Equipe deve ter pelo menos um membro")

    def __len__(self):
        return len(self.membros)

    def adicionar_membro(self, membro):

        if membro not in self.membros:
            self.membros.append(membro)
        else:
            print(f"Membro {membro} já está na equipe")

    def remover_membro(self, membro):

        if membro in self.membros:
            if len(self.membros) > 1:
                self.membros.remove(membro)
            else:
                raise ValueError("Não é possível remover o último membro da equipe")
        else:
            print(f"Membro {membro} não está na equipe")


def monitor(metodo):
    @wraps(metodo)
    def wrapper(self, acao):
        acao_normalizada = normalizar_texto(acao)
        if "autodestruicao" in acao_normalizada:
            raise RuntimeError("Ação proibida, autodestruição em curso...")

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_global[timestamp] = f"Missão de numero {self.numero_missao} executou {acao}"

        resultado = metodo(self, acao)
        resultado_normalizado = normalizar_texto(resultado)
        if "critico" in resultado_normalizado:
            print("⚠ Sistema em risco")

        return resultado
    return wrapper


@add_repr
class Missao:
    def __init__(self, numero_missao, planeta, equipe):
        self.numero_missao = validar_entrada(numero_missao, int, "numero_missao")
        self.planeta = validar_entrada(planeta, Planeta, "planeta")
        self.equipe = validar_entrada(equipe, Equipe, "equipe")
        
        if self.numero_missao in registro_missoes:
            raise ValueError(f"Missão número {numero_missao} já existe")
        
        registro_missoes[self.numero_missao] = self
        self.acao = None
        self.status = "criada"

    @monitor
    def executar(self, acao):
        self.acao = acao
        self.status = "executando"
        resultado = f"A ação '{self.acao}' será realizada no planeta {self.planeta.nome} pela equipe {self.equipe.nome}"
        self.status = "concluída"
        return resultado

    def cancelar(self):

        if self.status == "executando":
            raise RuntimeError("Não é possível cancelar uma missão em execução")
        self.status = "cancelada"
        print(f"Missão {self.numero_missao} foi cancelada")


def validar_entrada(valor, tipo_esperado, nome_campo):

    if not isinstance(valor, tipo_esperado):
        raise TypeError(f"{nome_campo} deve ser do tipo {tipo_esperado.__name__}, recebido {type(valor).__name__}")
    return valor


def auto_print(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        for item in resultado:
            print(item)
        return resultado
    return wrapper


@auto_print
def listar_missoes():
    return list(registro_missoes.values())


def obter_missao(numero):

    return registro_missoes.get(numero)


def listar_missoes_por_status(status):

    return [missao for missao in registro_missoes.values() if missao.status == status]


def estatisticas_missoes():

    total = len(registro_missoes)
    if total == 0:
        return "Nenhuma missão registrada"
    
    stats = {}
    for missao in registro_missoes.values():
        stats[missao.status] = stats.get(missao.status, 0) + 1
    
    return f"Total: {total} missões | " + " | ".join([f"{status}: {count}" for status, count in stats.items()])
#Testing Git