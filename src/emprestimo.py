from datetime import date

class Emprestimo:
    def __init__(self, id, usuario, livro, data_emprestimo=None):
        self.id = id
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo or date.today()
        self.data_devolucao = None
        self.status = "ativo"

    def registrar_devolucao(self):
        if self.status != "ativo":
            return False
        self.status = "devolvido"
        self.data_devolucao = date.today()
        self.livro.atualizar_disponibilidade(
            self.livro.quantidade_disponivel + 1
        )
        return True
