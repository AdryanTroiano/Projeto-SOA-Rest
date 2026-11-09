from flask import Blueprint, request, jsonify, make_response
from service.livro_service import LivroService
from model.livro import Livro

livro_bp = Blueprint("livro", __name__)

service = LivroService()

@livro_bp.route("/livro", methods=["GET", "POST", "PUT", "DELETE"])
def livro():

    if request.method == "POST":
        json = request.json
        livro = Livro(**json)
        service.cadastrar(livro)

        return jsonify({"mensagem": "Livro cadastrado!"})

    elif request.method == "PUT":
        json = request.json
        livro = Livro(**json)
        service.alterar(livro)

        return jsonify({"mensagem": "Livro atualizado!"})

    elif request.method == "DELETE":
        id = request.args.get("id", type=int)

        print("ID RECEBIDO PARA EXCLUSÃO:", id)

        service.excluir(id)

        print("LIVRO EXCLUÍDO COM SUCESSO!")

        return jsonify({"mensagem": "Livro excluído!"})

        return jsonify({"mensagem": "Livro excluído!"})

    livros = service.listar()
    return jsonify([livro.to_dict() for livro in livros])


@livro_bp.route("/getlivro")
def get_livro():
    id = request.args.get("id", type=int)
    livro = service.get_por_id(id)

    if livro:
        return jsonify(livro.to_dict())

    return make_response(
        jsonify({"mensagem": "Não encontrado!"}), 404
    )


@livro_bp.route("/getlivroid/<int:id>")
def get_livro2(id):
    livro = service.get_por_id(id)

    if livro:
        return jsonify(livro.to_dict())

    return make_response(
        jsonify({"mensagem": "Não encontrado!"}), 404
    )


@livro_bp.route("/getlivrotitulo")
def get_livro_titulo():
    titulo = request.args.get("titulo")
    livros = service.get_por_titulo(titulo)

    if livros:
        return jsonify([livro.to_dict() for livro in livros])

    return make_response(
        jsonify({"mensagem": "Não encontrado!"}), 404
    )


@livro_bp.errorhandler(ValueError)
def erro(mensagem):
    return make_response(
        jsonify({"mensagem": str(mensagem)}), 400
    )