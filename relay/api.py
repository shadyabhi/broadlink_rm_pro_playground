from flask import Flask
from flask_restful import Api
import resources


def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(resources.TVMode, '/tv/mode')
    api.add_resource(resources.TV, '/tv')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5678, debug=False)
