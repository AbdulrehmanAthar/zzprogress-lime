import requests
import pytest
import os

# Define the Docker Hub API endpoint and the Odoo image name and tag
DOCKERHUB_API = 'https://hub.docker.com/v2/repositories/library/odoo'
ODOO_IMAGE = 'odoo:latest'

# Define the Docker Hub credentials
username = os.environ.get('DOCKERHUB_USERNAME')
password = os.environ.get('DOCKERHUB_PASSWORD')

# Define the Jest test functions
def test_pull_odoo_image():
    # Send a GET request to the Docker Hub API to get the image details
    response = requests.get(DOCKERHUB_API)

    # Verify that the request was successful
    assert response.status_code == 200, f"Response status code was {response.status_code}, expected 200"

    # Parse the response JSON to get the image details
    image_details = response.json()

    # Verify that the image name and tag match the expected values
    assert image_details['name'] == 'odoo', f"Image name was {image_details['name']}, expected 'odoo'"
    assert image_details['full_description'].startswith('Odoo is a suite'), "Image description does not match expected value"

    # Send a GET request to the Docker Hub API to pull the Odoo image
    response = requests.get(f"https://hub.docker.com/v2/repositories/library/{ODOO_IMAGE}/dockerfile",
                            auth=(username, password))

    # Verify that the request was successful
    assert response.status_code == 200, f"Response status code was {response.status_code}, expected 200"

    # Parse the response JSON to get the Dockerfile contents
    dockerfile = response.json()['contents']

    # Verify that the Dockerfile contains the expected commands
    assert 'FROM python:3' in dockerfile, "Dockerfile does not contain expected base image"
    assert 'RUN pip install -r requirements.txt' in dockerfile, "Dockerfile does not contain expected pip command"
