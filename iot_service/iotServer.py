## Caution!!
## python 2.7
## run this code at raspberry pi

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import requests
import urlparse
import os
import settings_secret

IR = 'irsend SEND_ONCE '
MODEL = 'LGE_6711A20015N '
ircmd = ' '

class MyHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)

        ircmd = ' '
        
        if self.path == '/favicon.ico':
            ircmd=''
            return 

        elif self.path == '/':
            self.send_response(200)

        elif self.path[:3] == '/on':
            celsius = '22' if self.path[3:] == '' else self.path[3:]
            
            if int(celsius)<18:
                celsius = '18'

            if int(celsius)>30:
                celsius = '30'
                
            try:                
                ircmd = IR+MODEL+'UN-JEON/JEONG-JI_'+celsius
                os.system(ircmd)
                print "<ON>"
            except:
                print "<ON> cmd error"
            finally:
                self.send_response(200)

        elif self.path[:4] == '/set':
            celsius = '22' if self.path[4:] == '' else self.path[4:]
            
            if int(celsius)<18:
                celsius = '18'

            if int(celsius)>30:
                celsius = '30'
                
            try:                
                ircmd = IR+MODEL+'UN-JEON/JEONG-JI_'+celsius
                os.system(ircmd)
                print "<SET>"
            except:
                print "<SET> cmd error"
            finally:
                self.send_response(200)

        elif self.path == '/off':
            try:
                ircmd = IR+MODEL+'UN-JEON/JEONG-JI_OFF'
                os.system(ircmd)
                print "<OFF>"
            except:
                print "<OFF> cmd error"
            finally:
                self.send_response(200)

        elif self.path == '/super':
            try:
                ircmd = IR+MODEL+'PA-WEO-NAENG-BANG'
                os.system(ircmd)
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
        self.wfile.write('<h3>[recent command]<h3>')
        self.wfile.write('<h5>'+ircmd+'<h5>')
    
    def do_POST(self):
        self.send_response(404)

PORT = settings_secret.PORT

try:
    server = HTTPServer(('', PORT), MyHandler)
    print('Start server. port:', PORT)
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()