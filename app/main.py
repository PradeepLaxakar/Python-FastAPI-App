from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>Hello SPS Udaipur</h1><p>Standard FastAPI Process</p>"
