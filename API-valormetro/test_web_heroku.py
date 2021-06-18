import requests

def test_ok():

	resp = requests.get('https://imobpy.herokuapp.com/valormetro').json()
	assert resp['valormetro'] == "753.32"
