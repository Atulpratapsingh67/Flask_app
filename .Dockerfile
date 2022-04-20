FROM python
WORKDIR /Flasker
COPY . .
RUN pip install -r requirements.txt
CMD ["python","app.py"]
