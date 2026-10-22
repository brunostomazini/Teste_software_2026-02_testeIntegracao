class Sala:

    def __init__(
        self,
        nome,
        bloco,
        capacidade,
        id=None
    ):
        self.id = id
        self.nome = nome
        self.bloco = bloco
        self.capacidade = capacidade

    def __str__(self):
        return (f"Nome:{self.nome}, Bloco:{self.bloco}, ID:{self.id}")