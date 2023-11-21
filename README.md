# docker_flask_homework

##  Part 1


1. Setting Up and Dockerizing a Flask App:
   
First, create your repo, clone it into shell and cd into the correct window. For me it was docker_flask_homework. I went on to make sure the app.py had the code needed for the flask as well as my requirements had flask and my Dockerfile was set up properly so it could containerize the image. Comments are added as well as shown below explaining the dockerfile. 

I went on to build my dockerimage named maliha7.

<img width="572" alt="Screen Shot 2023-11-20 at 10 27 07 PM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/05031940-7a4d-404f-b201-19147a21c1f5">

In order to do this, I had to create my app.py run it and all other files(dockerfile and requirements). From here I  did docker build -t maliha 7 .

<img width="870" alt="Screen Shot 2023-11-20 at 11 27 33 PM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/337c809c-c32f-449b-86a5-d9c3ef19c11d">

After running this, you should have multiple rows of blue code, and this signifies that if it was built and the time it finished.

In this case my image is called maliha7 and a simple error I made in this was initially not adding my space period ( .) after

Subsequently, docker images shows me the image and to run I made sure I was in the correct port and ran the container with the code docker run -p 8005:5000 maliha7. 

A simple error I initally made was by having it was just -p and not including -d. In order to create that container, you have to include the -d which I did down below. 

<img width="872" alt="Screen Shot 2023-11-20 at 10 21 15 PM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/244eaf66-10ad-4359-9ac2-0921ca042fa5">

It succesfully ran and is accessible locally and I ensure this by changing my port to 8005. And here it says "Hello, this is the docker homework! From a Flask app in a Docker container!"

<img width="541" alt="Screen Shot 2023-11-20 at 10 20 51 PM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/5e931e71-005b-49eb-8208-0b67e5d46e1f">

This is running within the container, and this was verified by refreshing the page and the getting the get responses in our google shell. 

<img width="883" alt="Screen Shot 2023-11-20 at 10 22 42 PM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/1af8816f-625e-4480-8755-16de18dd6700">

The container for image 'maliha7' is called "45f198c3f7e79b938940c802caa6920cc6e48f6163c5615c382f88f210778fb7."

Additionally I ran multiple commands as well. 

Docker images shows the images I have created, in this case it is just maliha7
<img width="533" alt="Screen Shot 2023-11-20 at 10 58 14 PM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/4b3d70c7-09f0-4f43-84e7-98621b848128">

Docker ps also lets us view the containers we have. Here, it shows the container ID, image name, status, ports as well as a name fervent_pascal. 

<img width="877" alt="Screen Shot 2023-11-20 at 10 59 02 PM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/9fb114eb-9f8b-42ad-a341-8debc0a203a0">

In order to stop this, you write docker stop [container ID].

<img width="872" alt="Screen Shot 2023-11-20 at 11 04 52 PM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/dd5124f2-46d2-49f3-babf-306585ae3afa">

You can confirm that it has stopped by doing docker ps, and it will show you no containers running. In order to get it back up again you just do docker run -d -p and make sure your ports are the same as before. It is now up and running again. You can confirm this by doing docker ps, and it will show the status and generate a new name as well. 


These are the contents of my Dockerfile and comments.
#### This is the base image which comes from python and uses version 3.7. 
FROM python:3.7-alpine
#### this sets the working directory as /app. 
WORKDIR /app
#### copies what is in the directory into app container
COPY . /app
#### installs requirements file we need to run this, we have flask in our .txt
RUN pip install -r requirements.txt
#### Makes port 5000 open and accesible
EXPOSE 5000
#### CMD signifies the commands needed to run, in this case we are using python in our app.py file
CMD ["python", "app.py"]

## Part 2 Multi-Container Setup with Docker Compose


1. Preparing Two Flask Applications:

   
   I set up two different folders entitled flask1 and flask2. For flask1, my flaskapp tells you the date. For flask2, the flaskapp tells you the time including the date and time using seconds.

Date - connected and updates (loads to the date) 

<img width="480" alt="Screen Shot 2023-11-21 at 1 40 18 AM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/5201f1d0-43cd-4b87-bab6-9523cf381eff">


Time- connected and updates 
<img width="1013" alt="Screen Shot 2023-11-21 at 1 41 32 AM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/fbf77bf3-a618-4768-a3a8-1d0bf3a53294">


Once I made sure my flaskapps were running correctly and there were no connection errors, I did docker-compose up --build.

<img width="701" alt="Screen Shot 2023-11-21 at 2 13 04 AM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/f524b02a-e1cd-41ff-a174-1e2b1af33e0b">

And to get out of this, you do control c ( ^C) which will exit the applications.
<img width="794" alt="Screen Shot 2023-11-21 at 1 39 16 AM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/e004c2f2-63b0-46db-9a4f-92a3f9f4cb6f">


Once you do ^C, to get the apps back up and running you can do docker-compose up.

docker-compose up 
<img width="1017" alt="Screen Shot 2023-11-21 at 1 40 41 AM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/87814790-cdf2-4de5-a9e3-67f6776e0961">



But for some reason when I was intially runnong docker-compose up build , it wasnt saying running on all addresses. Instead showed one address and there were also some errors with the requirements files. I had gone into the Dockerfile and changed it into reuirements1 and requirements 2 to match the apps, however it was not being recognized and the apps were not running simultaneously.
From here,I made sure that my files were properly organized and neatly named so as to not run into this issue again. Once I changed those everything ran smoothly and as it should. 


<img width="988" alt="Screen Shot 2023-11-21 at 1 38 41 AM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/f948dcf5-f2de-4d22-ba4e-05b614460cd1">

The way I was able to fix this was by amending my Dockerfile, and from then on it was working properly. 

<img width="187" alt="Screen Shot 2023-11-21 at 2 16 57 AM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/9a1c3193-f1ba-47a1-b0fa-8970a66bcf8e">


More commands:

I am closing it down for the last time wih docker-compose down
<img width="748" alt="Screen Shot 2023-11-21 at 1 52 42 AM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/90074107-92ee-4b02-b684-096ce22a145c">

This was a screenshot taken prior to me closing the apps down. Nice, up and running!
<img width="953" alt="Screen Shot 2023-11-21 at 1 58 39 AM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/ac273fbb-017c-49d3-8c9c-246ed968d2e8">

I entered docker-compose down, it cannot connect! The apps are down. 
<img width="965" alt="Screen Shot 2023-11-21 at 1 59 27 AM" src="https://github.com/malh718/docker_flask_homework/assets/102617334/7056cfc2-7495-4364-bb45-3d9d4b59fa51">




