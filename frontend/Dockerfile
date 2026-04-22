FROM node:18-alpine

WORKDIR /app

# install dependencies
COPY package*.json ./
RUN npm install

# copy app
COPY . .

# non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

ENV PORT=3000
ENV API_URL=http://api:8000

EXPOSE 3000

CMD ["node", "app.js"]