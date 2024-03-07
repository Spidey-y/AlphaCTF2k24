FROM node:14

RUN groupadd -r ctfer && useradd -r -g ctfer -m -d /home/ctfer ctfer

WORKDIR /app

COPY package*.json ./

RUN npm install

RUN npm install cookie-parser --save && \
    npm install dotenv

COPY flag.txt .

COPY ./app/ .

RUN chmod 755 flag.txt && mv flag.txt /flag$(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 10).txt

EXPOSE 3000

USER ctfer

CMD ["node", "index.js"]
