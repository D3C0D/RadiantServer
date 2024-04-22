# RadiantServer
A simple HTTP server made with Python to serve static files without the need of installing anything. The goal for this was to have a simple, lightweight, trusty server that you could review the code of in 5 minutes to use with [ollama-chats](https://github.com/drazdra/ollama-chats). Maybe weird, but I didn't want to install a fully fledged server for something simple, so I developed this in my spare time.

# Main Features
- Extremely easy to use, quick to set up and lightweight.
- Simple code, peace of mind. You can glance at the source in 10 minutes and know your data is not stolen and shared! (Mainly because I don't know how to do that)
- Serves static files, this means HTML, JavaScript, CSS etc. So any basic page will work even with basic media files.
- Access on the same PC or over LAN on a different PC if connected to the same network.
- Can serve multiple pages at once, just put your project inside a folder inside the web folder, and it will be detected if it has an index.html file.
  Use this file structure: web/your_project/index.html

# How To Use exe on Windows
- Download the zip file from the releases page if you are on Windows
- Execute the RadiantServer.exe, and it will create a "web.config" file, a "web" folder and an "index.html" page by default.
- Once those are created, replace the index.html for yours and that is the one the server will serve.

# How To Run From Source
*If Python is not installed:*
- Just run "install.bat" to create a virtual environment with python on the folder (It will not install anything system-wide)
- Then run the "start.bat" to start the server on the virtual environment.

*If Python is installed:*
- The tool uses all standard libraries for its working, so if you use Python 3.9+ it should work just running the py file.

# Web.Config File
It contains some settings for the server, however they are not needed to work correctly.

- port : The port the server will use.
- address : The address the server will use (Set the IP from the PC to access it from inside the LAN)
- index_file : The name of the file that will be served. (I recommend leaving this as index.html, as that is the file that the server creates automatically)
*Note: the index.html file is not the one from your project, this is only a quick hub where you can choose from the pages hosted on the server.*

# Icon
The icon from the exe file is the Shallan Davar icon from her chapters on the Stormlight archive. Please, Brandon, don't take the project down :c
