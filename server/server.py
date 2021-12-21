from http.server import HTTPServer, BaseHTTPRequestHandler
import html, distr

tasklist = ["Task 1", "Task 2", "Task 3"]

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        temp = self.path.split('?')
        dict_args = {}
        try:
            args = temp[1].split("&")
            for i, arg in enumerate(args):
                args[i] = arg.split("=")
                temp2 = arg.split("=")
                dict_args[temp2[0]] = temp[1]
        except IndexError:
            args = []
        #print(temp[0])
        path = temp[0].split("/")
        #print(path, args)
        
        temp_path = "."
        for i in range(len(path)-1):    
            temp_path += path[i] + "/"
        
        prossesed = distr.distr(path, dict_args)
        if type(prossesed) == int:
            self.send_error(404)
        elif type(prossesed) == str:
            self.wfile.write(prossesed.encode())
        
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        print(self.post())



def main():
    PORT = 8000
    server = HTTPServer(('', PORT), requestHandler)
    print('<SERVER RUNNING> (port %s)' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()