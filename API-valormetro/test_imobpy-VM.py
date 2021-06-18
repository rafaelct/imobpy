import requests

def test_valor_minimo_valido():

  resp = requests.get('http://localhost:5001/valorimovel?qtdmetro=10').json()

  assert resp['valorimovel'] == "7533.20"
  assert resp['moeda'] == "R$"

def test_valor_maximo_valido():

  resp = requests.get('http://localhost:5001/valorimovel?qtdmetro=10000').json()

  assert resp['valorimovel'] == "7533200.00"
  assert resp['moeda'] == "R$"

def test_valor_minimo_invalido():

  resp = requests.get('http://localhost:5001/valorimovel?qtdmetro=9').json()  

  assert resp['erro'] == "Qtd. de metros deve estar entre 0 e 10000"

def test_valor_maximo_invalido():

  resp = requests.get('http://localhost:5001/valorimovel?qtdmetro=10001').json()  

  assert resp['erro'] == "Qtd. de metros deve estar entre 0 e 10000"

def test_valor_invalido():

  resp = requests.get('http://localhost:5001/valorimovel?qtdmetro=r').json()  

  assert resp['erro'] == "Valor invalido."
  assert resp['descricao'] == "could not convert string to float: 'r'"



