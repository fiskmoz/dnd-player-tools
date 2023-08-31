# Pull base image
FROM python:3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /api/

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /api/
RUN pipenv install --system --dev

COPY . /api/

EXPOSE 8000