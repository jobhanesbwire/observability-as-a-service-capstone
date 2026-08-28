FROM node:18-alpine
WORKDIR /usr/src/app

# Install dependencies
COPY package.json package-lock.json* ./
RUN npm install --production --no-audit --no-fund || true

# Copy source
COPY src/ ./src/

ENV PORT=3000
EXPOSE 3000

CMD ["node", "src/app.js"]
