class Pessoa:
    def __init__(self, nome, endereco, cpf, data_nascimento, genero, telefone):
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._genero = genero
        self._telefone = telefone

    # Getters
    def get_nome(self):
        return self._nome

    def get_endereco(self):
        return self._endereco

    def get_cpf(self):
        return self._cpf

    def get_data_nascimento(self):
        return self._data_nascimento

    def get_genero(self):
        return self._genero

    def get_telefone(self):
        return self._telefone

    # Setters
    def set_nome(self, nome):
        self._nome = nome

    def set_endereco(self, endereco):
        self._endereco = endereco

    def set_cpf(self, cpf):
        self._cpf = cpf

    def set_data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    def set_genero(self, genero):
        self._genero = genero

    def set_telefone(self, telefone):
        self._telefone = telefone