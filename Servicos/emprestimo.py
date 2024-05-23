from Pessoas import usuario,funcionario
from Livros import livro_fisico

class Emprestimo:
    def __init__(self,id_livro,id_usuario,id_funcionario,nome,edicao,isbn,prazo,entregue):
        super().__init__(id_livro,nome,edicao,isbn,id_usuario,id_funcionario)
        super().__init__(id_usuario)
        super().__init__(id_funcionario)
        self.prazo = prazo
        self.entregue = entregue