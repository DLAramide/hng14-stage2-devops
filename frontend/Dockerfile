# ---------- Stage 1: build ----------
FROM node:20-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .


# ---------- Stage 2: runtime ----------
FROM node:20-alpine

WORKDIR /app

# install wget for healthcheck
RUN apk add --no-cache wget

# create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# copy only necessary files
COPY --from=build /app /app

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 3000

HEALTHCHECK CMD wget --spider http://localhost:3000 || exit 1

CMD ["node", "app.js"]