# Build stage
FROM node:16-alpine3.15 as build-stage
WORKDIR /app
COPY ./package*.json ./
COPY ./yarn.lock ./
RUN yarn install
COPY ./ ./
RUN yarn build

# Production stage
FROM nginx:1.21.6-alpine
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY ./default.conf /etc/nginx/conf.d

