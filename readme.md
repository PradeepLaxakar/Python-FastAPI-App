## Port: 80 / 8000

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
docker build -t <USER-NAME>fast:v1 -f docker-files/Dockerfile .
```

```
docker run -p 8000:8000 <USER-NAME>fast:v1
```

# 4. Run in Azure Web app Linux Container

### Create web app with following specifications.
- Publish (Type) = Container

- Runtime stack = Python 3.14

- Operating System = Linux

- Image Source = ACR or dockerhub where image is located

- Leave startup command blank. Dockerfile has startup command.

# 5. Deploy using Azure Devops Pipeline on Azure Web App Linux Container

### Create web app with following specifications.
- *Image Source = Quickstart
-- We will create the web app using standard nginx image and push our image using pipeline.

- Port = 80

### Create a azure devops service connection with dockerhub so that pipeline can access dockerhub for image operations
*Dockerhub:*
- Account Settings > Personal access tokens > Generate New Token > Access Permission = Read & Write > Generate

*Azure Devops:*
- project Settings > Service connections > New service connection > Search > docker registry

- Registry type = Docker hub
- Docker ID = Your dockerhub userid
- Docker Password = Dockerhub PAT
- Service Connection Name = Meaningful name
- Verify and Save

### Create pipeline in Azure Devops
- Starter Pipeline
- Remove Content below "steps"

### Add docker steps in pipeline
- Show Assitant > Search > Docker
- Container repository = dockerhub_user-name/repo
- Add / Save 

```
steps:
- task: Docker@2
  inputs:
    containerRegistry: 'Docker-Hub-Dev7495-PAT'
    repository: 'dev7495/fast'
    command: 'buildAndPush'
    Dockerfile: '**/Dockerfile'
```

### Add Deployment steps to Azure web app
- Show assitant > Search > Azure Web App for Containers
- App Name = Select web app created
- Image name = Docker_user-name/image_name:$(Build.BuildId)
- Save and Run

```
steps:
- task: Docker@2
  inputs:
    containerRegistry: 'Docker-Hub-Dev7495-PAT'
    repository: 'dev7495'
    command: 'buildAndPush'
    Dockerfile: '**/Dockerfile'

- task: AzureWebAppContainer@1
  inputs:
    azureSubscription: 'Pay-As-You-Go (4f0e5ac1-0e6d-4ddf-a2f5-13eed2179f41)'
    appName: 'spsu'
    containers: 'dev7495/fast:$(Build.BuildId)'
```

### Verify changes
- It takes couple of minutes for changes to reflect in web app
