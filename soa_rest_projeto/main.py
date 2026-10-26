from flask import Flask
from flask_cors import CORS
from controller.livro_controller import livro_bp
from database import engine, Base

app = Flask(__name__)
CORS(app)

app.register_blueprint(livro_bp)

Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.run(port=9000, debug=True)