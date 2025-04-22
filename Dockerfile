FROM python:3.10  
WORKDIR /app
COPY . .
EXPOSE 5001
RUN pip install flask
CMD ["python", "server.py"]
