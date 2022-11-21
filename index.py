
# Modelo

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bem vindo ao Humanitar Dados'

@app.route('/buscar/<termo_de_busca>')
def buscar(termo_de_busca):
    nome_de_busca = str(termo_de_busca)
    return f'Você digitou ${nome_De_busca}'


if __name__ == "__main__":
	app.run(debug=False,Host='0.0.0.0')





