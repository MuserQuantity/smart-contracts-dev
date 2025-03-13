FROM node:18

USER node

RUN mkdir /home/node/.npm-global
RUN mkdir /home/node/source
ENV PATH=/home/node/.npm-global/bin:$PATH
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global

RUN npm i -g @remix-project/remixd@0.6.44
RUN sed -i s/127.0.0.1/0.0.0.0/g /home/node/.npm-global/lib/node_modules/@remix-project/remixd/src/websocket.js

EXPOSE 65520

ENTRYPOINT ["remixd", "-s", "/home/node/source", "--remix-ide", "https://remix.ethereum.org"]
