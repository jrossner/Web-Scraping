import json

with open('./test123.json', 'w') as outfile:
  outfile.write(json.dumps({'test': 'x'}))

file = json.load(open('./test123.json'))
print(file)
