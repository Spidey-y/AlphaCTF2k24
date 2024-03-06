FROM python:3.8

COPY challenge /challenge/

WORKDIR /challenge

RUN pip install -r requirements.txt

RUN adduser --disabled-password --force-badname alphaCTF && chmod 777 /challenge/

USER alphaCTF

EXPOSE 1337

ENTRYPOINT ["python", "-u", "bot.py"]
