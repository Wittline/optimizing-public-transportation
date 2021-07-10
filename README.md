# Monitoring the status of public Transportation with Apache Kafka
We will build an Streaming event pipeline around Kafka and its ecosystem that allows us to simulate and display the status of train lines in real time, using public data from the Chicago Transit Authority.

# Data Source
Public data from <a href="https://www.transitchicago.com/data/"> Chicago Transit Authority </a>

# Architecture

![image](https://user-images.githubusercontent.com/8701464/124824036-78558d00-df37-11eb-8db2-809633a05bd4.png)


#
# How to run the project with docker

- Install <a href="https://docs.docker.com/docker-for-windows/install/">Docker Desktop on Windows</a>, it will install **docker compose** as well, docker compose will alow you to run multiple containers applications
- Install <a href="https://www.stanleyulili.com/git/how-to-install-git-bash-on-windows/">git-bash for windows</a>, once installed , open **git bash** and download this repository, this will download the **docker-compose.yaml** file, and other files needed.

## Dependencies

- Kafka
- Zookeeper
- Schema Registry
- REST Proxy
- Kafka Connect
- KSQL
- Kafka Connect UI
- Kafka Topics UI
- Schema Registry UI
- Postgres

The docker-compose file does not run your code, to start docker-compose, navigate to the starter directory containing docker-compose.yaml and run the following commands using git bash:

```
$> cd starter
$> docker-compose up

Starting zookeeper          ... done
Starting kafka0             ... done
Starting schema-registry    ... done
Starting rest-proxy         ... done
Starting connect            ... done
Starting ksql               ... done
Starting connect-ui         ... done
Starting topics-ui          ... done
Starting schema-registry-ui ... done
Starting postgres           ... done
```

You will see a large amount of text print out in your terminal and continue to scroll. This is normal! This means your dependencies are up and running.

To check the status of your environment, you may run the following command at any time from a separate terminal instance:

```
$> docker-compose ps

            Name                          Command              State                     Ports
-----------------------------------------------------------------------------------------------------------------
starter_connect-ui_1           /run.sh                         Up      8000/tcp, 0.0.0.0:8084->8084/tcp
starter_connect_1              /etc/confluent/docker/run       Up      0.0.0.0:8083->8083/tcp, 9092/tcp
starter_kafka0_1               /etc/confluent/docker/run       Up      0.0.0.0:9092->9092/tcp
starter_ksql_1                 /etc/confluent/docker/run       Up      0.0.0.0:8088->8088/tcp
starter_postgres_1             docker-entrypoint.sh postgres   Up      0.0.0.0:5432->5432/tcp
starter_rest-proxy_1           /etc/confluent/docker/run       Up      0.0.0.0:8082->8082/tcp
starter_schema-registry-ui_1   /run.sh                         Up      8000/tcp, 0.0.0.0:8086->8086/tcp
starter_schema-registry_1      /etc/confluent/docker/run       Up      0.0.0.0:8081->8081/tcp
starter_topics-ui_1            /run.sh                         Up      8000/tcp, 0.0.0.0:8085->8085/tcp
starter_zookeeper_1            /etc/confluent/docker/run       Up      0.0.0.0:2181->2181/tcp, 2888/tcp, 3888/tcp

```

## Connecting to Services in Docker Compose

Now that your project’s dependencies are running in Docker Compose, we’re ready to get our project up and running. Windows Users Only: You must first install librdkafka-dev in your WSL Linux. 

Run the following command in your Ubuntu terminal:

```
sudo apt-get install librdkafka-dev -y
```


## Stopping Docker Compose and Cleaning Up

When you are ready to stop Docker Compose you can run the following command:

```
$> docker-compose stop
Stopping starter_postgres_1           ... done
Stopping starter_schema-registry-ui_1 ... done
Stopping starter_topics-ui_1          ... done
Stopping starter_connect-ui_1         ... done
Stopping starter_ksql_1               ... done
Stopping starter_connect_1            ... done
Stopping starter_rest-proxy_1         ... done
Stopping starter_schema-registry_1    ... done
Stopping starter_kafka0_1             ... done
Stopping starter_zookeeper_1          ... done
```


If you would like to clean up the containers to reclaim disk space, as well as the volumes containing your data:

```
$> docker-compose rm -v
Going to remove starter_postgres_1, starter_schema-registry-ui_1, starter_topics-ui_1, starter_connect-ui_1, starter_ksql_1, starter_connect_1, starter_rest-proxy_1, starter_schema-registry_1, starter_kafka0_1, starter_zookeeper_1
Are you sure? [yN] y
Removing starter_postgres_1           ... done
Removing starter_schema-registry-ui_1 ... done
Removing starter_topics-ui_1          ... done
Removing starter_connect-ui_1         ... done
Removing starter_ksql_1               ... done
Removing starter_connect_1            ... done
Removing starter_rest-proxy_1         ... done
Removing starter_schema-registry_1    ... done
Removing starter_kafka0_1             ... done
Removing starter_zookeeper_1          ... done
```
# Running the producer

```
cd producers
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python simulation.py
```
# Running the Faust Stream Processing Application
```
cd consumers
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
faust -A faust_stream worker -l info
```

# Running the KSQL Creation Script
```
cd consumers
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python ksql.py
```

# Running the consumer

```
cd consumers
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python server.py
```
