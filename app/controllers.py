from flask import request, jsonify
from app.models import db, Cocktail


def serialize_cocktail(cocktail):
    return {
        "id": cocktail.id,
        "name": cocktail.name,
        "ingredients": cocktail.ingredients,
        "instructions": cocktail.instructions,
    }


def get_cocktails():
    cocktails = Cocktail.query.all()
    serialized_cocktails = [serialize_cocktail(cocktail) for cocktail in cocktails]
    return jsonify(serialized_cocktails)


def get_cocktail(id):
    cocktail = db.session.get(Cocktail, id)
    if cocktail:
        return jsonify(serialize_cocktail(cocktail))
    return jsonify({"message": "Cocktail not found"}), 404


def create_cocktail():
    data = request.get_json()
    name = data.get("name")
    ingredients = data.get("ingredients")
    instructions = data.get("instructions")

    if name and ingredients and instructions:
        cocktail = Cocktail(
            name=name, ingredients=ingredients, instructions=instructions
        )
        db.session.add(cocktail)
        db.session.commit()
        return jsonify(serialize_cocktail(cocktail)), 201
    return jsonify({"message": "Missing required fields"}), 400


def delete_cocktail(id):
    cocktail = db.session.get(Cocktail, id)
    if cocktail:
        db.session.delete(cocktail)
        db.session.commit()
        return jsonify({"message": "Cocktail deleted successfully"}), 200
    return jsonify({"message": "Cocktail not found"}), 404
