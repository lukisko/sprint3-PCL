# sprint3-PCL

one of steps that you need to do in order to run this project outside of container is that you need to create venv using python in /venv 
(you can you also other names but then you want to change gitignore file and dockerignore file)

to start the project in docker you need to :
1. docker build -t flask-app .
2. docker run -dp 5000:5000 flask-app
