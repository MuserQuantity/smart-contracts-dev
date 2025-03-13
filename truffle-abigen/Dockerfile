FROM node:18

RUN apt-get update && apt-get install -y python3.10 python3-pip

RUN npm install -g truffle

RUN mkdir /etc/truffle
RUN mkdir /etc/truffle/contracts
WORKDIR /etc/truffle

COPY ./package.json .
COPY ./package-lock.json .
COPY ./truffle-config.js .

RUN npm install

