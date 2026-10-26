from database import Session
from model.livro import Livro

class LivroRepository:
    def __init__(self):
        self.__session = Session()

    def cadastrar(self, livro):
        self.__session.add(livro)
        self.__session.commit()
        self.__session.close()

    def listar(self):
        livros = self.__session.query(Livro).all()
        self.__session.close()
        return livros
    
    def get_por_id(self, id):
        livro = self.__session.get(Livro, id)
        self.__session.close()
        return livro
    
    def get_por_titulo(self, titulo):
        livros = self.__session.query(Livro).filter(
        Livro.titulo.like(f"%{titulo}%")
        ).all()
        self.__session.close()
        return livros