import requests, player
def start(ip:str):
    r = requests.get(ip+'start')
    vals = r.text.split(",")

    return player.Player([int(vals[0]), int(vals[1])], int(vals[2]), int(vals[3]), ip=ip)

def move(p):
    r = requests.get(f'{p.ip}upos-{p.id}:p:{p.pos[0]},{p.pos[1]}')
    print(r.text)
    
    enemies = []

    for vals in r.text.split('-'):
        e_vals = vals.split(':')
        pos = e_vals[1].split(',')
        p_id = e_vals[0]
        print(r.text, vals, e_vals, pos, p_id, p.id)
        if not int(p_id) == p.id:
            enemies.append(player.Player((int(pos[0]), int(pos[1])), 1, int(p_id)))

    return enemies

def shoot(p):
    if p.looking == 0 or p.looking == 3:
        mult = -1
    else:
        mult = 1

    if p.looking == 2 or p.looking == 0:
        # 0
        r = requests.get(f'{p.ip}shoot-{p.id}:d:{p.pos[0]+mult},{p.pos[1]}')

    else:
        # 1
        r = requests.get(f'{p.ip}shoot-{p.id}:d:{p.pos[0]},{p.pos[1]+mult}')

    enemies = []

    values = r.text.split('|')

    print(r.text, values)

    for vals in values[0].split("-"):
        e_vals = vals.split(':')
        pos = e_vals[1].split(',')
        p_id = e_vals[0]
        if not int(p_id) == p.id:
            enemies.append(player.Player((int(pos[0]), int(pos[1])), 1, int(p_id)))
        print(vals, e_vals, pos, p_id)

    p.kills = int(values[1])

    return enemies, p.kills


if __name__ == '__main__':
    p = player.Player((1, 4), 2, 1)
    r = move(p)
    print(r)
