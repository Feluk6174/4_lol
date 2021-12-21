from http.server import HTTPServer, BaseHTTPRequestHandler
import player

players = []

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global players
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        print(self.path)
        temp = self.path.split('-')
        if temp[0] == '/start':
            if len(players) == 0:
                pos = (1, 1)
            elif len(players) == 1:
                pos = (14, 1)
            elif len(players) == 2:
                pos = (1, 14)
            elif len(players) == 3:
                pos = (14, 14)
            players.append(player.Player(pos, 1, len(players)))

            self.wfile.write(bytes(f"{pos[0]},{pos[1]},1,{len(players)-1}", "utf-8"))
                

        if temp[0] == "/upos":
            temp = temp[1].split(':')
            values = temp[2].split(',')
            
            players[int(temp[0])].pos = [int(values[0]), int(values[1])]
            
            msg = ""
            for i, p in enumerate(players):
                if p.alive:
                    msg += f"{i}:{p.pos[0]},{p.pos[1]}-"
            print(msg[:-1:])
            self.wfile.write(bytes(msg[:-1:], "utf-8"))
            
        elif temp[0] == "/shoot":
            temp = temp[1].split(':')
            values = temp[2].split(',')
            msg = ""
            for i, p in enumerate(players):
                if not p.pos == [int(values[0]), int(values[1])] and p.alive:
                    msg += f"{i}:{p.pos[0]},{p.pos[1]}-"
                else:
                    players[int(temp[0])].kills += 1
                    p.alive = False
            print(msg[:-1:])
            self.wfile.write(bytes(msg[:-1:]+f"|{players[int(temp[0])].kills}", "utf-8"))
                

def main():
    PORT = 8000
    server = HTTPServer(('', PORT), requestHandler)
    print('<SERVER RUNNING> (port %s)' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()