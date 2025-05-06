from flask import Blueprint, request, redirect, jsonify
from models.url_model import init_db
from controllers.url_controller import create_short_url, resolve_short_url

url_blueprint = Blueprint('url', __name__)
init_db()

@url_blueprint.route('/api/shorten', methods=['POST'])
def api_shorten():
    data = request.get_json()
    original_url = data.get('url')

    if not original_url:
        return jsonify({'error': 'URL não fornecida'}), 400

    short_id = create_short_url(original_url)
    return jsonify({
        'short_url': f"http://localhost:5000/{short_id}",
        'code': short_id
    }), 201

@url_blueprint.route('/<short_id>', methods=['GET'])
def redirect_url(short_id):
    url = resolve_short_url(short_id)
    if url:
        return redirect(url)
    return jsonify({'error': 'URL não encontrada'}), 404
