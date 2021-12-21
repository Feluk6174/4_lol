import requests

r = requests.get('http://localhost:8000/start')
#r = requests.get('http://localhost:8000/upos-1:p:1,2')

#r = requests.get('http://localhost:8000/shoot-0:d:14,14')

def shoot():
    r = requests.get('http://localhost:8000/shoot-0:d:17,16')

    enemies = []

    values = r.text.split('|')

    print(r.text, values)

    for vals in values[0].split("-"):
        e_vals = vals.split(':')
        pos = e_vals[1].split(',')
        p_id = e_vals[0]
        #enemies.append(player.Player((int(pos[0]), int(pos[1])), 1, int(p_id)))
        print(vals, e_vals, pos, p_id)

    print(values[1])

shoot()

print(r, r.content.decode('utf-8'))