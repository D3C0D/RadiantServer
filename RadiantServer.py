from http.server import HTTPServer, BaseHTTPRequestHandler
import webbrowser
import configparser
import os

# Load configuration file at runtime or create one with default values if it doesn't exist
config = configparser.ConfigParser()
if not config.read('web.config'):
    # generate default values
    config.add_section('server')
    config.set('server', 'port', '8000')
    config.set('server', 'address', '')
    config.set('server', 'index_file', 'index.html')
    with open('web.config', 'w') as file:
        config.write(file)

# Create the web folder if it doesn't exist
web_folder_path = 'web'
if not os.path.exists(web_folder_path):
    os.makedirs(web_folder_path)
# Create the index.html file into the web folder if it doesn't exist
index_html_file_path = f'{web_folder_path}/{config.get('server', 'index_file')}'
if not os.path.exists(index_html_file_path):
    with open(index_html_file_path, 'w') as f:
        f.write('''
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <title>RadiantServer</title>
                    <style>
                        body {
                            background-color: #000;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            height: 100vh; /* Set the height of the page to match the screen height */
                            flex-direction: column; /* Stack elements vertically */
                        }
                        .container {
                            display: flex;
                            flex-direction: column;
                            align-items: center;
                        }
                        h1, h2 {
                            color: gold;
                            font-size: 64px;
                            text-align: center;
                        }
                        h2 {
                            color: green;
                            font-size: 52px;
                        }
                    </style>
                    </head>
                    <body>
                    <div class="container">
                        <h1>RadiantServer</h1>
                    </div>
                    <div class="container">
                        <h2>Is Online</h2>
                    </div>
                    </body>
                    </html>
                ''')

config = configparser.ConfigParser()
if not config.read('web.config'):
    # generate default values
    config.add_section('server')
    config.set('server', 'port', '8000')
    config.set('server', 'address', '')
    config.set('server', 'index_file', 'index.html')
    with open('web.config', 'w') as file:
        config.write(file)

class RadiantServerBaseHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        index_html = open("web/"+config.get('server', 'index_file'), 'r').read()
        self.wfile.write(index_html.encode('utf-8'))

if __name__ == "__main__":
    server_address = (config.get('server', 'address'), int(config.get('server', 'port')))
    httpd = HTTPServer(server_address, RadiantServerBaseHandler)
    print("RadiantServer is running...")
    webbrowser.open_new_tab(f'http://localhost:{httpd.server_port}/')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
         print("Server Stopped")
