# syntax=docker/dockerfile:1

FROM node:16-alpine3.15 AS builder

WORKDIR /app
COPY package.json package-lock.json ./

ARG API_URL

RUN npm i
COPY . .
RUN npm run build

CMD ["node","build"]