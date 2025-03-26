FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .
RUN  pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn" , "main:app" , "--host" , "0.0.0.0", "--port", "8000"]  