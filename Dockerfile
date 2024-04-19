FROM python:3.11
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install cryptography
COPY . /app
EXPOSE 8080
CMD ["python", "./main.py"]
