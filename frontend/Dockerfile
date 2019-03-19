# build stage
FROM node:lts-alpine as build-stage
WORKDIR /web

# copy both 'everything'
COPY web .

# install project dependencies
RUN npm install

# buld the app
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /web/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
