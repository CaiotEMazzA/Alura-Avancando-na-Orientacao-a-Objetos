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

class Programa:
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

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
