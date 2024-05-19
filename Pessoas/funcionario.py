from Pessoas.pessoa import Pessoa

class Funcionario (Pessoa):
    def __init__(self, id_funcionario, nome, endereco, cpf, data_nascimento, genero, telefone):
        super().__init__(nome, endereco, cpf, data_nascimento, genero, telefone)
        self._id_funcionario = id_funcionario
        
    # Get
    def get_id_funcionario(self):
        return self._id_carterina_funcionario
    
    # Set
    def set_id_funcionario(self, id_funcionario):
        self._id_funcionario = id_funcionario

    #Getters
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
        
    def __str__(self):
        return f'''Nome: {self.nome}, CPF: {self._cpf},Endereço: {self._endereco},
        Data de Nascimento: {self.data_nascimento}, 
        Gênero: {self.genero}, Telefone: {self._telefone}, 
        ID Carteirinha: {self._id_funcionario}'''

'''carlin = Funcionario('50','Carlos','rua das flores','11122233344455','03-05-1999','m',"1192222-5555")
print(carlin.__str__())
'''