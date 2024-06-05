from abc import ABC

class Pessoa(ABC):
    def __init__(self, nome, endereco, cpf, data_nascimento, genero, telefone):
        self.nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self.data_nascimento = data_nascimento
        self.genero = genero
        self._telefone = telefone

    # Getters
    @property
    def endereco(self):
        return self._endereco
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def telefone(self):
        return self._telefone

    #setters
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone