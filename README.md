# Monitoring the status of public Transportation with Apache Kafka
We will build an Streaming event pipeline around Kafka and its ecosystem that allows us to simulate and display the status of train lines in real time, using public data from the Chicago Transit Authority.

# Data Source
Public data from <a href="https://www.transitchicago.com/data/"> Chicago Transit Authority </a>

# Architecture

![image](https://user-images.githubusercontent.com/8701464/124824036-78558d00-df37-11eb-8db2-809633a05bd4.png)


# How to run the project

Install Docker Desktop on Windows, it will install docker compose as well, docker compose will alow you to run multiple containers applications,

Install git-bash for windows, once installed , open git bash and download this repository, this will download the dags folder and the docker-compose.yaml file, and other files needed.

1. Install docker and docker compose 

- Install <a href="https://www.stanleyulili.com/git/how-to-install-git-bash-on-windows/">git-bash for windows</a>, once installed , open **git bash** and download this repository, this will download the **dags** folder and the **docker-compose.yaml** file, and other files needed.




- Install <a href="https://docs.docker.com/docker-for-windows/install/">Docker Desktop on Windows</a>, it will install **docker compose** as well, docker compose will alow you to run multiple containers applications, Apache airflow has three main components: **metadata database**, **scheduler** and **webserver**, in this case we will use a celery executor too.



