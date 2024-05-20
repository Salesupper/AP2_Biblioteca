from livro import Livro

class Livro_digital(Livro):
    def __init__(self, id_livro, nome, isbn, editora, autor, qtd_paginas, nmr_edicao, genero, faixa_etaria, tamanho_mb, preco, disponivel=True, id_usuario=None):
        super().__init__(id_livro,nome,isbn,editora,autor,qtd_paginas,nmr_edicao,genero,faixa_etaria)
        self.tamanho_mb = tamanho_mb
        self.preco = preco
    
'''
#Testando
meu_Livro_digital = Livro_digital(8,"Aventuras no Espaço","4257-2","Editora X","Autor Y",200,1,"Ficção Científica",5,15,8.50)
#Testando 
print("Nome do Livro:", meu_Livro_digital.nome)
print("Editora:", meu_Livro_digital.editora)
print("Autor:", meu_Livro_digital.autor)
print("Número de Páginas:", meu_Livro_digital.qtd_paginas)
print("Número de Edição:", meu_Livro_digital.nmr_edicao)
print("Gênero:", meu_Livro_digital.genero)
print("Faixa Etária:", meu_Livro_digital.faixa_etaria)
print("Tamanho (MB):", meu_Livro_digital.tamanho_mb)
'''