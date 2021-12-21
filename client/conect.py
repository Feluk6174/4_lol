import requests, player
def move(p):
    r = requests.get(f'http://localhost:8000/upos-{p.id}:p:{p.pos[0]},{p.pos[1]}')
    print(r.text)

    res = []
    
    for val in r.text.split('-'):
        temp = val.split(':')
        values = temp[1].split(',')

        res.append([int(temp[0][-1]), int(values[0]), int(values[1])])

    return res

if __name__ == '__main__':
    p = player.Player((1, 4), 2, 1)
    r = move(p)
    print(r)
