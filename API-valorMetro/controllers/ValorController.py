#from models.Registry import Registry as ModelRegistry
#from controllers.utils.StatusReturn import StatusReturn
from flask import jsonify
#from controllers.utils.getKey import getKey

class ValorController :

    def methodGet(self,request) :
        
        #registration = ModelRegistry()

        #data = request.get_json(silent=True)

        #login = getKey(data,"loginname")
        #password = getKey(data,"password")
        #fullname = getKey(data,"fullname")

        #login = request.args.get("loginname")
        #password = request.args.get("password")
        #fullname = request.args.get("fullname")

        #statusReturn = StatusReturn()

        # Valor vindo do banco de dados
        valor = 753.32

        dados = {}

        #dados['valormetro2'] = "{:.2f}".format(valor)
        dados['valormetro'] = format(valor, '.2f')
        return dados

        
        #try :
        #    registration.add(login=login,password=password,fullname=fullname)
        #    
        #    return jsonify( statusReturn.getStatus(codReturn=0,msgReturn="Success") )
        #except Exception as error :
            
        #    return statusReturn.getStatus(codReturn=1,msgReturn=str(error) )

