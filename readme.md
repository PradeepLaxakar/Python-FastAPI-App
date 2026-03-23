# 1. Run in local (Win11)
Open your terminal in the project folder and run these commands: 

## Install dependencies:
```
pip install -r requirements.txt
```

## Start the server
```
uvicorn app.main:app --reload
```

## OR 

## Start without reload
```
uvicorn app.main:app 
```

# 2. Run in Azure Web app (Code)
#### Connection = Repo

## startup command
```
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

# 3. Run in container in local
```
docker build -t fast:v1 -f docker-files/Dockerfile .
```

# 4. Run in Azure Web app (Container)
#### Connection = Repo
