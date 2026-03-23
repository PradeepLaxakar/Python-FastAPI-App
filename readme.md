# Run in local (Win11)
Open your terminal in the project folder and run these commands: 

## Install dependencies:
pip install -r requirements.txt

## Start the server
uvicorn app.main:app --reload

## OR 

## Start without reload
uvicorn app.main:app 

# Run in Azure Web app (Python). Type = Code | Connection = Repo
## startup command
gunicorn -w 2 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 app.main:app

