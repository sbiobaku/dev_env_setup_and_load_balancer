FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
VOLUME [ "/app" ]

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

CMD python3 -m gunicorn --bind 0.0.0.0:5000 wsgi:app --reload