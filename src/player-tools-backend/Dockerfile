# Pull base image
FROM python:3.12

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /api

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /api/
RUN pipenv install --system --dev

EXPOSE 8000