# RadiantServer
A simple HTTP server made with Python to run basic HTML files without the need of installing anything.

# How To Use
- Just download the exe file from the releases page if you are on Windows, execute it, and it will create a "web.config" file, a "web" folder and an "index.html" page by default.
- Once those are created, replace the index.html for yours and that is the one the server will serve.

# How To Run From Source
The tool uses all standard libraries for its working, so if you use Python 3.9+ it should work just running the py file.

# Web.Config File
It contains some settings for the server, however they are not needed to work correctly.

[server]
port : The port the server will use
address : The address the server will use
index_file : The name of the file that will be served.

