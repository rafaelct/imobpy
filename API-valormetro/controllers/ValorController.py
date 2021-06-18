from flask import jsonify

class ValorController :

    def methodGet(self,request) :

        # Valor vindo do banco de dados
        valor = 753.32

        dados = {}

        
        dados['valormetro'] = format(valor, '.2f')
        return dados

        
