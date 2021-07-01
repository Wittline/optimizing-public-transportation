"""Producer base-class providing common utilites and functionality"""
import logging
import time


from confluent_kafka import avro
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka.avro import AvroProducer

logger = logging.getLogger(__name__)


class Producer:
    """Defines and provides common functionality amongst Producers"""

    # Tracks existing topics across all Producer instances
    existing_topics = set([])

    def __init__(
        self,
        topic_name,
        key_schema,
        value_schema,
        num_partitions=1,
        num_replicas=1,
    ):
        """Initializes a Producer object with basic settings"""
        self.topic_name = topic_name
        self.key_schema = key_schema
        self.value_schema = value_schema
        self.num_partitions = num_partitions
        self.num_replicas = num_replicas


        self.broker_properties = {
            "bootstrap.servers": "PLAINTEXT://localhost:9092",
            "schema.registry.url": "http://localhost:8081",
        }

        # If the topic does not already exist, try to create it
        if self.topic_name not in Producer.existing_topics:
            self.create_topic()
            Producer.existing_topics.add(self.topic_name)

        self.producer = AvroProducer(
            self.broker_properties,
            default_value_schema = value_schema,
            default_key_schema = key_schema,        
        )

    def create_topic(self):
        """Creates the producer topic if it does not already exist"""
        
        cli = AdminClient({"bootstrap.servers": self.broker_properties["bootstrap.servers"]})

        t_metadata = cli.list_topics()
        if self.topic_name in t_metadata.topics:
            logger.info(f'Topic {self.topic_name} already exist')
            return
        
        logger.info(f'New Topic {self.topic_name} will be create')

        ntopic = cli.create_topics([NewTopic(topic=self.topic_name, num_partitions= self.num_partitions, replication_factor=self.num_replicas)])

        for t, nt in ntopic.items():
            try:
                nt.result()
                logger.info("Topic created: %s ", t)
            except Exception as e:
                logger.error("Error creating topic: %s: due to %s", t, e)

    def close(self):
        """Prepares the producer for exit by cleaning up the producer"""
        if self.producer:
            self.producer.flush()

    def time_millis(self):
        """Use this function to get the key for Kafka Events"""
        return int(round(time.time() * 1000))
