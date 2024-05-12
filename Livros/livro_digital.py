from Livros.livro_fisico import Livro_fisico

class Livro_digital(Livro_fisico):
    def __init__(self, nome_livro, nome_editora, nome_autor, qtd_paginas, nmr_edicao, tipo_capa, tipo_genero, faixa_etaria, tamanho_gb, preco):
        super().__init__(nome_livro, nome_editora, nome_autor, qtd_paginas, nmr_edicao, tipo_capa, tipo_genero, faixa_etaria)
        self.tamanho_gb = tamanho_gb
        self.preco = preco
    
    # Getters    
    def get_tamanho_gb(self):
        return self.tamanho_gb
    
    def get_preco(self):
        return self.preco

    # Setters
    def set_tamanho_gb(self, tamanho_gb):
        self.tamanho_gb = tamanho_gb
        
    def set_preco(self, preco):
        self.preco = preco
        
# # Testando set
# meu_Livro_digital = Livro_digital("", "", "", 0, 0, "", "", "", 0)
# meu_Livro_digital.set_nome_livro("Aventuras no Espaço")
# meu_Livro_digital.set_nome_editora("Editora X")
# meu_Livro_digital.set_nome_autor("Autor Y")
# meu_Livro_digital.set_qtd_paginas(200)
# meu_Livro_digital.set_nmr_edicao(1)
# meu_Livro_digital.set_tipo_capa("Digital")
# meu_Livro_digital.set_tipo_genero("Ficção Científica")
# meu_Livro_digital.set_faixa_etaria("Livre")
# meu_Livro_digital.set_tamanho_gb(10)

# # testando get
# print("Nome do Livro:", meu_Livro_digital.get_nome_livro())
# print("Editora:", meu_Livro_digital.get_nome_editora())
# print("Autor:", meu_Livro_digital.get_nome_autor())
# print("Número de Páginas:", meu_Livro_digital.get_qtd_paginas())
# print("Número de Edição:", meu_Livro_digital.get_nmr_edicao())
# print("Tipo de Capa:", meu_Livro_digital.get_tipo_capa())
# print("Gênero:", meu_Livro_digital.get_tipo_genero())
# print("Faixa Etária:", meu_Livro_digital.get_faixa_etaria())
# print("Tamanho (GB):", meu_Livro_digital.get_tamanho_gb())

# # testando get e set para int
# meu_Livro_digital.set_tamanho_gb(15)
# print("\nTamanho modificado (GB):", meu_Livro_digital.get_tamanho_gb())