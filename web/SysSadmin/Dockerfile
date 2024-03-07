FROM node:14

RUN groupadd -r appgroup && useradd -r -g appgroup appuser

WORKDIR /app
COPY ./app/package*.json ./

RUN npm install

RUN npm install dotenv

COPY ./app .

RUN chmod 744 flag.txt  && mv flag.txt /flag$(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 20).txt

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 3000

CMD ["node", "index.js"]
