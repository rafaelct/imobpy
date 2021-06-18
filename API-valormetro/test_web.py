import requests

def test_ok():

	resp = requests.get('http://localhost:5000/valormetro').json()
	assert resp['valormetro'] == "753.32"
