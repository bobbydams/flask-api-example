from flask import Blueprint, jsonify

from apps.api.domain.library import DomainException

APP_NAME = "Flask Example"
bp = Blueprint("api", __name__, url_prefix="")


@bp.errorhandler(DomainException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    response.code = error.code
    return response