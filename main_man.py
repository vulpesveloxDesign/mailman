import random

#todo:
#find flere efternavne

boys_names = []
girls_names = []
sur_names = []
mail_addies = [
    'hotmail.com',
    'gmail.com',
    'yahoo.com',
    'dinmorerenjunkieso.dk',
    'takforsidst.dk',
    'viglemmeraldrig.dk',
    'cia.gov',
    #div email vendors her...
    ]
connectors = [
    #research: findes der flere lovlige typer?
    '_',
    '',
    '',
    '',
    '.',
    ]

with open('names_b.txt', 'r') as bnames:
    for name in bnames.read().splitlines():
        boys_names.append(name)

with open('names_g.txt', 'r') as gnames:
    for name in gnames.read().splitlines():
        girls_names.append(name)

with open('last_names.txt', 'r') as lnames:
    for name in lnames.read().splitlines():
        sur_names.append(name)

print(len(boys_names))
print(len(girls_names))
print(len(sur_names))

for i in range(40):
    print(random.choice(boys_names)+ random.choice(connectors) + random.choice(sur_names)+ '@' + random.choice(mail_addies))
