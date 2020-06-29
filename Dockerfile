FROM python:3.8.2
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /writing_service

# Install dependencies
COPY Pipfile Pipfile.lock /writing_service/
RUN pip install pipenv && pipenv install --system
# Copy project
COPY . /writing_service/