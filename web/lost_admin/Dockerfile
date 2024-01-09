FROM node:14

WORKDIR /app

COPY challenge/package.json .

RUN npm install

COPY . .

EXPOSE 1337

WORKDIR /app/challenge

CMD ["npm", "start"]

