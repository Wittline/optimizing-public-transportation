"""Defines core consumer functionality"""
import logging

import confluent_kafka
from confluent_kafka import Consumer
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError
from tornado import gen


logger = logging.getLogger(__name__)


class KafkaConsumer:
    """Defines the base kafka consumer class"""

    def __init__(
        self,
        topic_name_pattern,
        message_handler,
        is_avro=True,
        offset_earliest=False,
        sleep_secs=1.0,
        consume_timeout=0.1,
    ):
        """Creates a consumer object for asynchronous use"""
        self.topic_name_pattern = topic_name_pattern
        self.message_handler = message_handler
        self.sleep_secs = sleep_secs
        self.consume_timeout = consume_timeout
        self.offset_earliest = offset_earliest

        self.broker_properties = {
            'bootstrap.servers': 'PLAINTEXT://localhost:9094',
            'default.topic.config': {'auto.offset.reset': 'earliest'},
            'group.id': topic_name_pattern            
        }

        if is_avro is True:
            self.broker_properties["schema.registry.url"] = "http://localhost:8081"
            self.consumer = AvroConsumer(self.broker_properties)
        else:
            self.consumer = Consumer(self.broker_properties)
            pass

        
        self.consumer.subscribe([topic_name_pattern],on_assign=self.on_assign)

    def on_assign(self, consumer, partitions):
        """Callback for when topic assignment takes place"""
        for p in partitions:
            consumer.seek(p)
        logger.info(f"partitions assigned for {self.topic_name_pattern}")
        consumer.assign(partitions)


    async def consume(self):
        """Asynchronously consumes data from kafka topic"""
        while True:
            num_results = 1
            while num_results > 0:
                num_results = self._consume()
            await gen.sleep(self.sleep_secs)

    def _consume(self):
        """Polls for a message. Returns 1 if a message was received, 0 otherwise"""
        try:
            msg = self.consumer.poll(timeout=1.0)
            if msg is not None:
                if msg.error() is not None:
                    self.message_handler(msg)
                    return 1
                else:
                    logger.error(msg.error())
                    return 0
            else:
                logger.debug("no message")
                return 0
        except SerializerError as error:
            logger.error(f"Error consuming data: {error.message}")
            return 0


    def close(self):
        self.consumer.close()
