import os
import socket
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    # 1. Check if we are in Azure
    azure_site = os.getenv("WEBSITE_SITE_NAME")
    
    # 2. Check if we are in a Docker Container
    is_docker = os.path.exists("//.dockerenv")
    
    # 3. Determine the "Friendly" location
    if azure_site:
        location = f"☁️ Azure Web App ({azure_site})"
    elif is_docker:
        location = f"🐳 Docker Container (ID: {socket.gethostname()})"
    else:
        location = f"💻 Local Machine ({socket.gethostname()})"

    return f"""
    <html>
        <body style="font-family: sans-serif; text-align: center; padding-top: 50px;">
            <h1>Hello Lovely People :)</h1>
            <h1>Welcome to Pradeep's Training</h1>
            <h2 style="color: #0078d4;">This App is running on: {location}</h2>
            <p>Standard FastAPI Process</p>
        </body>
    </html>
    """
