# Madplanlaegger
This is a tool to ease the process of constructing a grocery list, when planning multiple meals with common ingredients.

It is a simple web application written in python utilizing the plotly dash package.

Recipes are stored in an excel spreadsheet.

## Installation and setup
The repository in structured to run the application in a docker container, so make sure docker is installed and running.

First step is to open some sort of terminal in the repository directory.

Then we build the app's container image, this is done with the following command
```
docker build -t madplanlaegger .
```
The `-t` flag is for tag and the string that comes next will be the name of the container.
The first time the image is built from scratch it will take forever to install pandas and numpy, but subsequent builds seem to be faster.

Second step is then to start a container based on the image just build, this is done with the following command
```
docker run -dp 8050:8050 madplanlaegger
```
The `-dp` tells docker that we want to run the container in detached mode (in other words, headless or in the background) as well as map port 8050 of the container to port 8050 on the host.
