from pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, id_usuario, nome, endereco, cpf, data_nascimento, genero, telefone):
        super().__init__(nome, endereco, cpf, data_nascimento, genero, telefone)
        self._id_usuario = id_usuario
        
    # Get
    @property
    def id_usuario(self):
        return self._id_usuario

    # Set
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    def __str__(self):
        return f'''Nome: {self.nome}, CPF: {self._cpf},Endereço: {self._endereco},
        Data de Nascimento: {self.data_nascimento}, 
        Gênero: {self.genero}, Telefone: {self._telefone}, 
        ID Carteirinha: {self._id_usuario}'''

carlin = Usuario(50,'Carlos','rua das flores','422-222','03-05-1999','m','1192222-5555')
print(carlin.__str__())