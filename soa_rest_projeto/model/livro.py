from sqlalchemy import Column, Integer, String
from database import Base

class Livro(Base):
    __tablename__ = "livro"

    id = Column(Integer, autoincrement=True, primary_key=True)
    titulo = Column(String(100), nullable=False)
    autor = Column(String(100), nullable=False)
    isbn = Column(String(20), nullable=False)
    ano = Column(Integer, nullable=False)

    def __init__(self, titulo: str, autor: str, isbn: str, ano: int):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano = ano

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn,
            "ano": self.ano
        }