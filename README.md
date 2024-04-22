# RadiantServer
A simple HTTP server made with Python to run basic HTML files without the need of installing anything.

# How To Run From Source
*If Python is not installed:*
- Just run "install.bat" to create a virtual environment with python on the folder (It will not install anything system-wide)
- Then run the "start.bat" to start the server on the virtual environment.

*If Python is installed:*
- The tool uses all standard libraries for its working, so if you use Python 3.9+ it should work just running the py file.

# How To Use exe on Windows
*Due to the use of PyInstaller, there is a false positive on the exe, run from source if you don't trust it*
- Just download the exe file from the releases page if you are on Windows, execute it, and it will create a "web.config" file, a "web" folder and an "index.html" page by default.
- Once those are created, replace the index.html for yours and that is the one the server will serve.

# Web.Config File
It contains some settings for the server, however they are not needed to work correctly.

[server]
port : The port the server will use
address : The address the server will use
index_file : The name of the file that will be served.

# Icon
The icon is the Shallan Davar icon from her chapters on the Stormlight archive. Please, Brandon, don't take the project down :c
