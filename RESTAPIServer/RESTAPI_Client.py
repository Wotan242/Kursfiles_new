import requests
import json
import sys
x = sys.argv[1]
op = sys.argv[2]
y = sys.argv[3]
try:

	IP = sys.argv[4]

except IndexError:

	IP = 'localhost'

print(op)

payload = { 'x' : str(x) , 'y' : str(y)}
myheaders = {'content-type' : 'application/json'}

if op == '+':

	url = 'http://%s:5000/v1/ressources/calculator/add' % IP

if op == '-':

	url = 'http://%s:5000/v1/ressources/calculator/sub' % IP





resp = requests.post(url , data = json.dumps(payload) , headers = myheaders)

print(resp.json())