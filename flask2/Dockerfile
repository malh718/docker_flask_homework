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
