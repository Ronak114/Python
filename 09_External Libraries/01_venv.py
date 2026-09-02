# to install : pip install packageName


# Virtual Environment (venv): is a tool to create isolated Python environments. It allows you to manage dependencies for different projects separately.

# virtual env solves the problem of dependency conflicts between different projects. It allows you to create a self-contained environment for each project, with its own set of packages and dependencies.

# install - pip install virtualenv
# create - python -m venv env_name
# activate - .\env_name\Scripts\Activate.ps1"
# deactivate - deactivate.


# Requirements file: A requirements file is a text file that lists all the dependencies required for a Python project.
# pip freeze > requirements.txt


# Requests library: Python library for making HTTP requests. It provides a simple and intuitive API for sending HTTP requests and handling responses.

import requests

r = requests.get("https://www.google.com")

with open("code.txt", "w") as f:
    f.write(r.text)
