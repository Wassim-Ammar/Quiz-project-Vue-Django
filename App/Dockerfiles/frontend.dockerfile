# build stage
FROM node:18.18.1-alpine as build-stage
WORKDIR /app
COPY App/frontend/package*.json ./
RUN npm install
COPY ./App/frontend .
RUN npm run build

# production stage  
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY App/Dockerfiles/nginx/default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]