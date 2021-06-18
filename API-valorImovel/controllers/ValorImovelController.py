#from models.Registry import Registry as ModelRegistry
#from controllers.utils.StatusReturn import StatusReturn
#from flask import jsonify
#from controllers.utils.getKey import getKey
from config.Config import url_api_valormetro
import requests

class ValorImovelController :

    def methodGet(self,request) :
        
        #registration = ModelRegistry()

        #data = request.get_json(silent=True)

        #qtdMetro = getKey(data,"qtdmetro")



        #password = getKey(data,"password")
        #fullname = getKey(data,"fullname")

        resposta = {}

        qtdMetro = request.args.get("qtdmetro")

        try:

            qtdMetro = float(qtdMetro)

        except ValueError as e:
            dados = {}
            dados['erro'] = 'Valor invalido.'
            dados['descricao'] = str(e)
            return dados

        if qtdMetro < 10 or qtdMetro > 10000 :
            resposta['erro'] = 'Qtd. de metros deve estar entre 0 e 10000'
            return resposta
            
        print("Qtd. do metro:")
        print(qtdMetro)

        resp = requests.get(url_api_valormetro).json()

        print(resp['valormetro'])
        
        valorImovel = float(resp['valormetro']) * qtdMetro
        
        

        

        dados = []

        resposta['valorimovel'] = format(valorImovel, '.2f')
        resposta['moeda'] = 'R$'

        return resposta
        
        