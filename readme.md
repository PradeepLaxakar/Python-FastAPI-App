# Install and Run
Open your terminal in the project folder and run these commands: 

## Install dependencies:
pip install -r requirements.txt

## Start the server
uvicorn app.main:app --reload

## OR 

## Start without reload
uvicorn app.main:app 