from http.server import HTTPServer, BaseHTTPRequestHandler
import configparser
import json
import mimetypes
import os
import webbrowser

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
index_html_file_path = f'{web_folder_path}/{config.get("server", "index_file")}'
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
                h1 {
                    color: gold;
                    font-size: 64px;
                    text-align: center;
                }
                h2 {
                    color: green;
                    font-size: 42px;
                }
                h4 {
                    color: white;
                    font-size: 22px;
                }
                #folderSelect {
                    margin-top: 20px;
                    width: 300px; /* Set the width of the combo box */
                    height: 40px; /* Set the height of the combo box */
                    font-size: 16px; /* Set the font size of the options */
                }
            </style>
            <script>
                window.onload = function() {
                    var folderSelect = document.getElementById('folderSelect');

                    fetch('/folders')
                    .then(response => response.json())
                    .then(data => {
                        data.folders.forEach(folder => {
                            var option = document.createElement('option');
                            option.text = folder;
                            folderSelect.add(option);
                        });
                    });

                    folderSelect.addEventListener('change', function() {
                        var selectedFolder = folderSelect.value;
                        if (selectedFolder !== '') {
                            window.location.href = '/' + selectedFolder + '/index.html';
                        }
                    });
                };
            </script>
            </head>
            <body>
            <div class="container">
                <h1>RadiantServer</h1>
            </div>
            <div class="container">
                <h2>Is Online</h2>
            </div>
            <div class="container">
                <h4>Choose the page to load:</h4>
            </div>
            <div class="container">
                <select id="folderSelect">
                    <option value="" disabled selected>Select a folder</option>
                </select>
            </div>
            </body>
            </html>
        ''')

# Serve static files, and handle redirection for default dir
class RadiantServerBaseHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
            return

        if self.path == '/folders':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            folders = [folder for folder in os.listdir(web_folder_path) if os.path.isdir(os.path.join(web_folder_path, folder))]
            response_data = {'folders': folders}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
            return

        # Serve static files
        file_path = os.path.join(web_folder_path, self.path[1:])
        if os.path.exists(file_path):
            # Set appropriate MIME type
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type:
                self.send_response(200)
                self.send_header('Content-type', mime_type)
                self.end_headers()

                # Serve the file
                with open(file_path, 'rb') as file:
                    self.wfile.write(file.read())
            else:
                self.send_error(415, 'Unsupported Media Type')
        else:
            self.send_error(404, 'File Not Found')

if __name__ == "__main__":
    server_address = (config.get('server', 'address'), int(config.get('server', 'port')))
    httpd = HTTPServer(server_address, RadiantServerBaseHandler)
    print("RadiantServer is running...")
    webbrowser.open_new_tab(f'http://localhost:{httpd.server_port}/index.html')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
         print("Server Stopped")
