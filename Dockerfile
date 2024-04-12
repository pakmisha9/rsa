FROM python:3.11
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install cryptography
RUN #pip install requirements.txt
COPY . /app
CMD ["python", "./main.py"]