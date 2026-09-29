class Usuario:
    def __init__(self, id, nome, cpf, email, nivel_acesso="usuario"):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.ativo = True
        self.nivel_acesso = nivel_acesso

    def consultar_acervo(self, catalogo, criterio):
        return catalogo.pesquisar(criterio)
