# Step 1: Build the site
FROM node:18-alpine AS builder

WORKDIR /app
COPY imranslab-web/ .
RUN npm install && npm run build

# Step 2: Serve with NGINX
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]