FROM python:3.11-slim
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the "app" folder into the container
COPY ./app ./app

# Run from the /code directory
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
