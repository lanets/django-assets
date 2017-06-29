FROM python:3.5
ENV PYTHONUNBUFFERED 1

# Add the working directory
RUN mkdir /opt/django-assets
WORKDIR /opt/django-assets

# Requirement file creation
ADD requirements.txt /opt/django-assets
RUN pip install -r requirements.txt

ADD . /opt/django-assets
