FROM node:22-alpine3.20

EXPOSE 3000

COPY app .
COPY *.json .

RUN npm install && npm run-script build

CMD npm run-script start