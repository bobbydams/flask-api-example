from datetime import datetime

from flask import request
from flasgger import validate
from flasgger.utils import swag_from
from flask_jwt_extended import jwt_required

from apps.api.app import bp
from apps.api.context import Context
from apps.api.domain import commands, model

context = Context()


@bp.route("/book", methods=["POST"])
@jwt_required
@swag_from("specs/book_add.yml", methods=["POST"])
def add():
    validate(request.json, "BookSchema", "specs/book_add.yml")
    data = request.json
    book = model.Book(
        title=data["title"],
        author=data["author"],
        publisher=data["publisher"],
        pages=data["pages"],
    )
    command = commands.AddBook(book=book)
    context.messagebus.handle(command)
    return dict(success=True), 200


@bp.route("/book/<title>", methods=["GET"])
@jwt_required
@swag_from("specs/book_get.yml", methods=["GET"])
def get(title):
    command = commands.GetBook(title=title)
    book = context.messagebus.handle(command)
    return book, 200


@bp.route("/book", methods=["PUT"])
@jwt_required
@swag_from("specs/book_put.yml", methods=["PUT"])
def update():
    validate(request.json, "BookSchema", "specs/book_put.yml")
    data = request.json
    book = model.Book(
        title=data["title"],
        author=data["author"],
        publisher=data["publisher"],
        pages=data["pages"],
    )
    command = commands.UpdateBook(book=book)
    result = context.messagebus.handle(command)
    return dict(success=result), 201


@bp.route("/book/<title>", methods=["DELETE"])
@jwt_required
@swag_from("specs/book_delete.yml", methods=["DELETE"])
def delete(title):
    command = commands.DeleteBook(title=title)
    result = context.messagebus.handle(command)
    return dict(success=result), 200