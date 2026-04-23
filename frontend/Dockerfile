# ---------- Stage 1: deps ----------
FROM node:20-alpine AS deps

WORKDIR /app

COPY package*.json ./
RUN npm install --only=production


# ---------- Stage 2: runtime ----------
FROM node:20-alpine

WORKDIR /app

# create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# copy dependencies
COPY --from=deps /app/node_modules ./node_modules

# copy app source
COPY . .

# fix permissions
RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 3000

CMD ["node", "app.js"]