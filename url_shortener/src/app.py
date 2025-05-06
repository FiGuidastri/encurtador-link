from flask import Flask
from views.url_view import url_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(url_blueprint)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
