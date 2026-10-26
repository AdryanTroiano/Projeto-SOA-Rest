from flask import Blueprint, request, jsonify, make_response
from service.livro_service import LivroService
from model.livro import Livro

livro_bp = Blueprint("livro", __name__)

service = LivroService()

@livro_bp.route("/livro", methods=["GET", "POST"])
def livro():
    if request.method == "POST":
        json = request.json
        livro = Livro(**json)
        service.cadastrar(livro)
        return jsonify({"mensagem": "Livro cadastrado!"})

    livros = service.listar()
    return jsonify([livro.to_dict() for livro in livros])


@livro_bp.errorhandler(ValueError)
def erro(mensagem):
    return make_response(
        jsonify({"mensagem": f"{mensagem}"}),
        500
    )