from repository.livro_repository import LivroRepository

class LivroService:
    def __init__(self):
        self.__repository = LivroRepository()

    def cadastrar(self, livro):
        if len(livro.titulo) > 100:
            raise ValueError("O título deve ter até 100 caracteres.")

        if len(livro.autor) > 100:
            raise ValueError("O autor deve ter até 100 caracteres.")

        if len(livro.isbn) > 20:
            raise ValueError("O ISBN deve ter até 20 caracteres.")

        if livro.titulo == "" or livro.autor == "" or livro.isbn == "":
            raise ValueError("Todas as informações devem ser preenchidas.")

        if livro.ano <= 0:
            raise ValueError("O ano deve ser maior que zero.")

        self.__repository.cadastrar(livro)

    def listar(self):
        return self.__repository.listar()
    
    def get_por_id(self, id):
        return self.__repository.get_por_id(id)