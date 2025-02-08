from flask import Flask
from configuration import configure_all

# inicialização
app = Flask(__name__)

configure_all(app)

# execução
if __name__ == '__main__':
    app.run(debug=True)
