#base image
FROM python:3.9-slim
#thisis the working directory inside the container
WORKDIR /app
#copying the requirements file to the working directory
COPY requirements.txt .
#installing the dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt
#copying the application code to the working directory
COPY app.py .
#the port on which the application will run inside the container
EXPOSE 8000
#commands to run the application using uvicorn
CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000" ]
