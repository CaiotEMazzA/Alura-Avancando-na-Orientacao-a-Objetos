# Conceito da herança em Orientação a Objetos: quando eu quero que exista mais de uma classe com atributos/métodos
# iguais, eu crio uma classe mais 'genérica' com tudo o que as minhas outras classes vão herdar em comum. Neste código,
# essa classe 'genérica' é a classe 'Programa'.

# Atributos e métodos privados não são herdados pela classe filha. Para resolver o problema de acessar esses atributos
# nas classes herdeiras, convencionou-se o uso de apenas um underscore. Assim, o atributo não sofre o name mangling
# (name mangling = _nomedaclasse__atributo) e se comporta como um atributo normal, podendo ser usado em outras classes.
# Lembrando que o underscore único ainda indica que esse atributo deve ser considerado como 'privado'.

# OBS.: A classe-mãe é chamada também de superclasse.

# Para não precisar inicializar atributos iguais em cada classe herdeira, pode-se utlilizar o comando
# 'super().__init__(<parâmetros comuns entre superclasse e classe herdeira>)' para aproveitar os atributos em comum dos
# objetos da classe alvo.
# O método 'super()' pode chamar qualquer método ou atributo da classe mãe.

# Assim como temos atributos ligados diretamente às classes, também temos métodos. As duas formas de criar tais métodos
# são:
#
# - Métodos de classe, utilizando o decorator '@classmethod'. Quando criamos um método de classe, temos acesso aos
# atributos da classe. Assim como podemos acessar os atributos de classe por meio dos atributos de instâncias, podemos
# acessar os métodos de classe por meio dos métodos de instância. Exemplo:
#######################################################################################################################
# class Funcionario:
#     prefixo = 'Instrutor'
#
#     @classmethod
#     def info(cls):
#         return f'Esse é um {cls.prefixo}'
#######################################################################################################################
#
# - Métodos estáticos, utilizando o decorator @staticmethod. Nesse caso, não é possível acessar as informações da
# classe, porém o método estático é acessível a partir da classe e também da instância. Exemplo:
#######################################################################################################################
# class FolhaDePagamento:
#     @staticmethod
#     def log():
#         return f'Isso é um log qualquer'
#######################################################################################################################

# Classes filhas são do mesmo tipo que a classe mãe. Isso significa, no exemplo deste código, que o Filme É UM
# Programa, que a Série É UM Programa, mas o Filme NÃO É UMA Série e vice versa. Tendo a classe mãe em comum, podemos
# fazer, por exemplo, um loop em uma lista com objetos de diferentes classes filhas de uma mesma classe mãe pedindo
# para imprimir os atributos relativos à classe mãe.

# O python tem uma função que retorna um booleano indicando se um objeto tem um certo tipo de atributo. Essa função é a
# 'hasattr(<objeto>, <atributo procurado>)'.

# O conceito de Duck Typing diz que um objeto não precisa ser de um tipo para usar comportamentos daquele tipo. Por
# exemplo, se uma ave anda como pato, nada como pato e tem bico de pato, eu não preciso me preocupar se ela é um pato
# ou não. Da mesma forma, o python não está interessado se um objeto é de determinado tipo. Desde que ele tenha os
# mesmos comportamento que aquele tipo, o python executa tal comportamento.

# O método dunder '__getitem__' pode fazer com que um objeto se torne iterável mesmo sem herdar da classe 'list'.

from abc import ABCMeta, abstractmethod

class Programa(metaclass = ABCMeta):
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @abstractmethod
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


procurando_nemo = Filme('Procurando nemo', 2003, 100)
mandaloriano = Serie('O Mandaloriano', 2019, 2)
tmep = Filme('Todo mundo em pânico', 1999, 120)
demolidor = Serie('Demolidor', 2016, 4)

procurando_nemo.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
mandaloriano.dar_like()
mandaloriano.dar_like()

filmes_e_series = [procurando_nemo, mandaloriano, demolidor, tmep]
minha_playlist = Playlist('Fim de Semana', filmes_e_series)

print(f'Tamanho da playlist: {len(minha_playlist)} programas.')

for programa in minha_playlist:
    print(programa)

print(f'Tá ou não tá? {demolidor in minha_playlist}')
