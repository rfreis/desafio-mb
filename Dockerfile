# Base Image
FROM python:3.7

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# install environment dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

# Install project dependencies
RUN pipenv --python 3.7
RUN pipenv install --system --deploy --skip-lock 

EXPOSE 8000
CMD gunicorn docs.wsgi:application --bind 0.0.0.0:8000
