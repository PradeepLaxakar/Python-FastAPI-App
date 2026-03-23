# 1. Run in local (Win11)
Open your terminal in the project folder and run these commands: 

## Install dependencies:
pip install -r requirements.txt

## Start the server
uvicorn app.main:app --reload

## OR 

## Start without reload
uvicorn app.main:app 

# 2. Run in Azure Web app (Code). 
#### Connection = Repo

## startup command
gunicorn -w 2 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 app.main:app

# 3. Run in Azure Web app (Container). 
#### Connection = Repo

