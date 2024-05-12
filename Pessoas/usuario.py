from Pessoas.pessoa import Pessoa

class Usuario (Pessoa):
    def __init__(self, nome, endereco, cpf, data_nascimento, genero, telefone, id_carterinha_usuario):
        super().__init__(nome, endereco, cpf, data_nascimento, genero, telefone)
        self._id_carterina_usuario = id_carterinha_usuario
        
    # Getters
    def get_id_carterina_usuario(self):
        return self._id_carterina_usuario
    
    # Setters
    def set_id_carterina_usuario(self, id_carterinha_usuario):
        self._id_carterina_usuario = id_carterinha_usuario