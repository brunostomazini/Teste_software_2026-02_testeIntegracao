from Sala import Sala
from SalaDAO import SalaDAO


class SalaService:
    def __init__(self, dao):
        self.dao = dao



    def valida_sala_nome(self ):
        if self.nome.strip() == "" or self.nome == None:
            raise ValueError("Nome da sala não pode estar em branco.")
        
    def valida_sala_bloco(self, ):
        if self.bloco.strip() == "" or self.bloco == None:
            raise ValueError("Bloco não pode estar em branco.")

    def valida_sala_capacidade(self):
        if not isinstance(self.capacidade, int):
            raise ValueError("Nome da sala não pode estar em branco.")
        elif not (1 <= self.capacidade <=100):
            raise ValueError ("Nome da sala não pode estar em branco.")
    
    def unicidade_de_sala(self):
        salaCadastrada = self.dao.buscar_por_nome_bloco(self.nome, self.bloco)
        if self.nome == salaCadastrada.nome and self.bloco == salaCadastrada.bloco:
            raise ValueError("Nome da sala não pode estar em branco.")

    def cadastra_sala(self):
        self.valida_sala_nome(self.nome)
        self.valida_sala_bloco(self.bloco)
        self.valida_sala_capacidade(self.capacidade)
        self.unicidade_de_sala(self.id)
    
    def busca_sala_id():
        pass
    
    def lista_sala():
        pass

    def atualiza_sala():
        pass

    def exclui_sala():
        pass

    def encerra_acesso():
        pass
    
    def injecao_dependecia():
        pass