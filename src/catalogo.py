class Catalogo:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def alterar_livro(self, livro):
        for i, item in enumerate(self.livros):
            if item.id == livro.id:
                self.livros[i] = livro
                return True
        return False

    def pesquisar(self, criterio):
        criterio = criterio.lower()
        return [
            livro for livro in self.livros
            if criterio in livro.titulo.lower()
            or criterio in livro.autor.lower()
            or criterio in livro.isbn.lower()
            or criterio in livro.categoria.lower()
        ]

    def verificar_disponibilidade(self, livro):
        return livro.esta_disponivel()
