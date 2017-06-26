FROM python:3

# Add the working directory
ADD . /opt/django-assets
WORKDIR /opt/django-assets

# Requirement file creation
ADD requirements.txt /opt/django-assets
RUN pip install -r requirements.txt
