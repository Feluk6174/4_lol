from http.server import HTTPServer, BaseHTTPRequestHandler
import player

p_1 = player.Player((1, 1), 2)
p_2 = player.Player((17, 17), 2)

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global p_1, p_2
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        print(self.path)
        temp = self.path.split('-')
        print(temp)
        if temp[0] == "/upos":
            temp = temp[1].split(':')
            values = temp[2].split(',')
            if temp[0] == "1":
                p_1.pos = [int(values[0]), int(values[1])]
            elif temp[1] == "2":
                p_2.pos = [int(values[0]), int(values[1])]
            print(temp, values)
            self.wfile.write(bytes(f"p_1:{p_1.pos[0]},{p_1.pos[1]}-p_2:{p_2.pos[0]},{p_2.pos[1]}", "utf-8"))
        elif temp[0] == "/shoot":
            temp = temp[1].split(':')
            values = temp[2].split(',')
            p_list = (p_1, p_2)
            msg = ""
            for i, p in enumerate(p_list):
                if not p.pos == [int(values[0]), int(values[1])]:
                    msg += f"p_{i+1}:{p.pos[0]},{p.pos[1]}-"

            self.wfile.write(bytes(msg[:-1:], "utf-8"))
                

def main():
    PORT = 8000
    server = HTTPServer(('', PORT), requestHandler)
    print('<SERVER RUNNING> (port %s)' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()