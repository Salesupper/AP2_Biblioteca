from pessoas import Usuario
from livros import livro_digital

class Aluguel:
    def __init__(self,id_livro,id_usuario,nome,edicao,isbn,prazo,preco):
        super().__init__(id_livro,nome,edicao,isbn)
        super().__init__(id_usuario)
        self.prazo = prazo
        self.preco = preco