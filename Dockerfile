FROM python:3.10-alpine
WORKDIR /Flasker
COPY . .
RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt
CMD ["python","app.py"]
