from abc import(ABC)

class Livro(ABC):
    def __init__(self, id_livro, nome, isbn, editora, autor, qtd_paginas, nmr_edicao, genero, faixa_etaria, disponivel=True, id_usuario=None):
        self.id_livro = id_livro
        self.nome = nome
        self.isbn = isbn
        self.editora = editora
        self.autor = autor
        self.qtd_paginas = qtd_paginas
        self.nmr_edicao = nmr_edicao
        self.genero = genero
        self.faixa_etaria = faixa_etaria
        self.disponivel = disponivel
        self.id_usuario = id_usuario
        
'''
book = Livro('1989','77722-2','oeste','george',217,5,'normal','distopico',18)
print(book.nome_autor)
print(book.isbn)
'''