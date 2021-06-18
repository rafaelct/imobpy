from flask import Flask, jsonify, request
from controllers.ValorImovelController import ValorImovelController
import os

app = Flask(__name__)

@app.route("/valorimovel", methods=['GET'])
def epValorGET():
    valorImovelController = ValorImovelController()

    try:

        return valorImovelController.methodGet(request=request)

    except Exception as e:
        dados = {}
        dados['erro'] = 'Erro interno, tente mais tarde.'
        dados['descricao'] = e
        return dados


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0',port=port)
