class livro_fisico:
    def __init__(self, nome_livro, nome_editora, nome_autor, qtd_paginas, nmr_edicao, tipo_capa, tipo_genero, faixa_etaria):
        self.nome_livro = nome_livro
        self.nome_editora = nome_editora
        self.nome_autor = nome_autor
        self.qtd_paginas = qtd_paginas
        self.nmr_edicao = nmr_edicao
        self.tipo_capa = tipo_capa
        self.tipo_genero = tipo_genero
        self.faixa_etaria = faixa_etaria
    
    def set_nome_livro(self, nome_livro):
        self.nome_livro = nome_livro
        
    def get_nome_livro(self):
        return self.nome_livro
    
    def set_nome_editora(self, nome_editora):
        self.nome_editora = nome_editora
        
    def get_nome_editora(self):
        return self.nome_editora
    
    def set_nome_autor(self, nome_autor):
        self.nome_autor = nome_autor
        
    def get_nome_autor(self):
        return self.nome_autor
        
    def set_qtd_paginas(self, qtd_paginas):
        self.qtd_paginas = qtd_paginas
        
    def get_qtd_paginas(self):
        return self.qtd_paginas
    
    def set_nmr_edicao(self, nmr_edicao):
        self.nmr_edicao = nmr_edicao
        
    def get_nmr_edicao(self):
        return self.nmr_edicao
    
    def set_tipo_capa(self, tipo_capa):
        self.tipo_capa = tipo_capa
        
    def get_tipo_capa(self):
        return self.tipo_capa
    
    def set_tipo_genero(self, tipo_genero):
        self.tipo_genero = tipo_genero
        
    def get_tipo_genero(self):
        return self.tipo_genero
    
    def set_faixa_etaria(self, faixa_etaria):
        self.faixa_etaria = faixa_etaria
        
    def get_faixa_etaria(self):
        return self.faixa_etaria