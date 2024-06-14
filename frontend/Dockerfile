ARG NODE_VERSION=22

FROM node:${NODE_VERSION}-alpine as base

WORKDIR /app
COPY . .
# Да сборка непраивльная, это сделано для быстрого поднятия фронта на локалке, без установки локакльной nodejs
RUN npm i
RUN npm ci
RUN npm run build

FROM node:${NODE_VERSION}-alpine

WORKDIR /app

COPY --from=base /app/.output /app

ENV HOST 0.0.0.0
ENV PORT 3000

EXPOSE 3000

CMD ["node", "./server/index.mjs"]