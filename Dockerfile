FROM python:3.10-alpine3.15

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD ["app.py"]