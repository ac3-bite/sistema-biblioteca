from src.livro import Livro
from src.catalogo import Catalogo

def test_pesquisa_por_titulo():
    catalogo = Catalogo()
    livro = Livro(1, "Python para Iniciantes", "Autor Teste",
                  "123", "Editora", 2026, "Programação", 1)
    catalogo.adicionar_livro(livro)
    resultado = catalogo.pesquisar("python")
    assert len(resultado) == 1
    assert resultado[0].titulo == "Python para Iniciantes"
