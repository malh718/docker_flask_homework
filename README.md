# docker_flask_homework

# 1. Setting Up and Dockerizing a Flask App:


These are the contents of my Dockerfile and comments.
# This is the base image which comes from python and uses version 3.7
FROM python:3.7-alpine
# this sets the working directory as /app. 
WORKDIR /app
# copies what is in the directory into app container
COPY . /app
# installs requirements file we need to run this, we have flask in our .txt
RUN pip install -r requirements.txt
#Makes port 5000 open
EXPOSE 5000
# CMD signifies the commands needed to run, in this case we are using python in our app.py file
CMD ["python", "app.py"]

I went on to build my dockerimage named maliha7$

/Screen Shot 2023-11-20 at 10.27.07 PM.png

In order to do this, I had to create my app.py run it and all other files(dockerfile and requirements). From here I i did docker build -t maliha 7 .

In this case my image is called maliha7 and a simple error I made in this was initially not adding my space period ( .) after

Subsequently, docker images shows me the image and to run I made sure I was in the correct port and ran the container with the code docker run -p 8005:5000 maliha7. 

It succesfully ran and is accessible locally and I ensure this by changing my port to 8005. And here it says "Hello, this is the docker homework! From a Flask app in a Docker container!"

This is running within the container, and this was verified by refreshing the page and the getting the get responses in our google shell. 


