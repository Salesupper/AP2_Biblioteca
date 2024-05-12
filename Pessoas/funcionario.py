from Pessoas.pessoa import Pessoa

class Funcionario (Pessoa):
    def __init__(self, nome, endereco, cpf, data_nascimento, genero, telefone, id_carterinha_funcionario):
        super().__init__(nome, endereco, cpf, data_nascimento, genero, telefone)
        self._id_carterina_funcionario = id_carterinha_funcionario
        
    # Getters
    def get_id_carterina_funcionario(self):
        return self._id_carterina_funcionario
    
    # Setters
    def set_id_carterina_funcionario(self, id_carterinha_funcionario):
        self._id_carterina_funcionario = id_carterinha_funcionario
        
    def __str__(self):
        return f"Nome: {self._nome}, CPF: {self._cpf}, Endereço: {self._endereco}, Data de Nascimento: {self._data_nascimento}, Gênero: {self._genero}, Telefone: {self._telefone}, ID Carteirinha: {self._id_carterina_funcionario}"