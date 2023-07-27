from flask import Blueprint
from .controllers import get_cocktails, get_cocktail, create_cocktail, delete_cocktail

cocktail_bp = Blueprint("cocktail", __name__)


@cocktail_bp.route("/cocktails", methods=["GET"])
def get_all_cocktails():
    return get_cocktails()


@cocktail_bp.route("/cocktails/<int:id>", methods=["GET"])
def get_single_cocktail(id):
    return get_cocktail(id)


@cocktail_bp.route("/cocktails", methods=["POST"])
def add_cocktail():
    return create_cocktail()


@cocktail_bp.route("/cocktails/<int:id>", methods=["DELETE"])
def remove_cocktail(id):
    return delete_cocktail(id)
