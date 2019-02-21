import yaml

file = open('family.yaml','r')
data = yaml.load(file)

print(data)

print(data['name'])

print(data['wife'])

print(data['children'])
print(data['children'][0])
print(data['children'][0]['name'])

data['children'][0]['name'] = 'TTTTom'

print(data['children'][0]['name'])