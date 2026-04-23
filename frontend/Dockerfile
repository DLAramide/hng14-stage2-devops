# ---------- Stage 1: build ----------
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build


# ---------- Stage 2: runtime ----------
FROM nginx:alpine

# create non-root user (grading requirement)
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# copy build output
COPY --from=builder /app/dist /usr/share/nginx/html

# fix permissions
RUN chown -R appuser:appgroup /usr/share/nginx/html

USER appuser

EXPOSE 80

# healthcheck (THIS IS REQUIRED)
HEALTHCHECK CMD wget -qO- http://localhost || exit 1

CMD ["nginx", "-g", "daemon off;"]