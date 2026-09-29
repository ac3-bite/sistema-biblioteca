class Livro:
    def __init__(self, id, titulo, autor, isbn, editora, ano_publicacao,
                 categoria, quantidade_disponivel=1):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.editora = editora
        self.ano_publicacao = ano_publicacao
        self.categoria = categoria
        self.quantidade_disponivel = quantidade_disponivel
        self.situacao = "disponível" if quantidade_disponivel > 0 else "indisponível"

    def esta_disponivel(self):
        return self.quantidade_disponivel > 0

    def atualizar_disponibilidade(self, quantidade):
        self.quantidade_disponivel = max(0, quantidade)
        self.situacao = "disponível" if self.quantidade_disponivel > 0 else "indisponível"

        def __str__(self):
        return f"{self.titulo} - {self.autor} | ISBN: {self.isbn} | Situação: {self.situacao}"