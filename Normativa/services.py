import requests
import time

def getNormativas(filterVar):
	url = 'http://localhost:8000/api/normativa'
	print('filtro:' + filterVar)
	params = {'nombre': filterVar}
	r = ''
	while r == '':
		try:
			r = requests.get(url, params=params)
			break
		except:
			time.sleep(5)
			continue
	#r = requests.get(url, params=params)
	normativas = r.json()	
	return normativas
