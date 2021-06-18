from flask import Flask, request
from controllers.ValorController import ValorController
#from controllers.Auth import Auth
#from controllers.Customers import Customers
#from controllers.Products import Products
#from controllers.Carts import Carts
#from controllers.Orders import Orders
import os

app = Flask(__name__)

@app.route("/valormetro", methods=['GET'])
def epValorPOST():
    valorController = ValorController()

    return valorController.methodGet(request=request)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port)
