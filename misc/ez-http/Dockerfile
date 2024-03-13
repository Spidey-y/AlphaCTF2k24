FROM node:20-alpine

RUN mkdir -p /home/node/app/ && chown -R node:node /home/node/app

WORKDIR /home/node/app

USER node

COPY --chown=node:node . .

EXPOSE 8000

CMD [ "node", "server.js" ]

