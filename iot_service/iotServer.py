## Caution!!
## python 2.7
## run this code at raspberry pi

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import requests
import urlparse
import os

# LG ir command
def irCmd(func, arg='', model='LGE_6711A20015N'):
    '''
    air conditional command translator
    default model is 'LGE_6711A20015N'
    '''
    if func.isnumeric():
        arg = func
        func = 'UN-JEON/JEONG-JI_'
    return 'irsend SEND_ONCE '+model+' '+func+arg

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)

        #print self.path
        if self.path == '/favicon.ico':
            return 

        elif self.path[:3] == '/on':
            celsius = '22' if self.path[3:] == '' else self.path[3:]
            try:
                tempCmd = irCmd('UN-JEON/JEONG-JI_', celsius)
                os.system(tempCmd)
                print "<ON> " + celsius
            except:
                print "<ON> cmd error"
            finally:
                self.send_response(200)
                print(celsius)

        elif self.path == '/cold':
            celsius = self.path[5:]
            try:
                tempCmd = irCmd('UN-JEON/JEONG-JI_', celsius)
                os.system(tempCmd)
                print "<COLD> " + celsius
            except:
                print "<COLD> cmd error"
            finally:
                self.send_response(200)
                print(celsius)

        elif self.path == '/off':
            try:
                tempCmd = irCmd('UN-JEON/JEONG-JI_', 'OFF')
                os.system(tempCmd)
                print "<OFF>"
            except:
                print "<OFF> cmd error"
            finally:
                self.send_response(200)

        elif self.path == '/super':
            try:
                tempCmd = irCmd('PA-WEO-NAENG-BANG')
                os.system(tempCmd)
                print "<SUPER>"
            except:
                print "<SUPER> cmd error"
            finally:
                self.send_response(200)

        else:
            print "cmd not found"
            self.send_response(405)

        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write('<h1>ECC IOT Service</h1>')
        self.wfile.write('<h2 style="color:green">status: green</h2>')
    
    def do_POST(self):
        self.send_response(404)

PORT = ## PORT NUMBER ##

try:
    server = HTTPServer(('', PORT), MyHandler)
    print('Start server. port:', PORT)
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()