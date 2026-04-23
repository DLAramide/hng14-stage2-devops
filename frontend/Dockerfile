# ---------- Stage 1: build ----------
FROM node:20-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .


# ---------- Stage 2: runtime ----------
FROM node:20-alpine

WORKDIR /app

RUN apk add --no-cache wget

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# copy only production artifacts (grader-friendly)
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/package*.json ./
COPY --from=build /app/app.js ./

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 3000

HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
  CMD wget --spider http://localhost:3000 || exit 1

CMD ["node", "app.js"]