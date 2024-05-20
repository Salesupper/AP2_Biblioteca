from livro import Livro

class Livro_fisico(Livro):
    def __init__(self, id_livro, nome, isbn, editora, autor, qtd_paginas, nmr_edicao, genero, faixa_etaria, tipo_capa, disponivel=True, id_usuario=None):
        super().__init__(id_livro,nome,isbn,editora,autor,qtd_paginas,nmr_edicao,genero,faixa_etaria)
        self.tipo_capa = tipo_capa

'''
book = Livro_fisico(1,'1984','77722-2','São carlos','George','271',3,'ficção',18,'dura',True,9)
print(book.tipo_capa)
print(book.id_livro)
print(book.id_usuario)
'''        
