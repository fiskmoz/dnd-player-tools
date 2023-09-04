# Use an official Node.js LTS (Long Term Support) Alpine Linux image as the base image
FROM node:lts-alpine

# Set environment variables
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# Install Bash in the container
RUN apk update && apk add bash

WORKDIR /web

# Copy only the package.json and package-lock.json files and install dependencies
COPY package*.json ./

#Install dependecies
RUN npm i

# Copy the rest of your project files into the container
COPY . .

# Expose the port your application listens on
EXPOSE 5173