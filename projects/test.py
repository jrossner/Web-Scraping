import json

with open('./test123.json', 'w') as outfile:
  outfile.write(json.dumps({'test': 'x'}))
