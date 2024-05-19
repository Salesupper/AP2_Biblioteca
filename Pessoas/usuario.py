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



carlin = Usuario(50,'Carlos','rua das flores','422-222','03-05-1999','m','1192222-5555')

#usando get
# print(carlin.get_id_usuario())

#usando @property
print(carlin.id_usuario)

#usando set
# carlin.set_id_usuario(12)
# print(carlin.id_usuario)

#usando setter
carlin.id_usuario = 20
print(carlin.id_usuario)


