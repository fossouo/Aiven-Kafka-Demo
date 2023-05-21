import time
import json
import random
import uuid
from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka import KafkaAdminClient

# Kafka broker configuration
bootstrap_servers = 'kafka-30215ae9-fossouodonald-dd11.aivencloud.com:23761'
topic = 'aiven_topic_dfp'

# SSL certificate paths
cafile = '/Users/marbofinance/Downloads/fledge-north-kafka-python-develop/test_clients/ca.pem'
certfile = '/Users/marbofinance/Downloads/fledge-north-kafka-python-develop/test_clients/service.cert'
keyfile = '/Users/marbofinance/Downloads/fledge-north-kafka-python-develop/test_clients/service.key'

# Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    security_protocol='SSL',
    ssl_cafile=cafile,
    ssl_certfile=certfile,
    ssl_keyfile=keyfile,
)

# Function to generate random IoT data
def generate_iot_data():
    # Generate a random UUID as key
    key = str(uuid.uuid4())

    # Generate random IoT data
    data = {
        'sensor_id': key,
        'temperature': round(random.uniform(20.0, 40.0), 2),
        'humidity': round(random.uniform(30.0, 80.0), 2),
        'timestamp': int(time.time())
    }

    return key, data

# Kafka producer delivery callback
def delivery_callback(err, msg):
    if err:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic} [{msg.partition}]')

# Start producing messages
while True:
    # Generate random IoT data
    key, data = generate_iot_data()

    # Serialize data to JSON
    message = json.dumps(data).encode('utf-8')

    # Produce message to Kafka
    producer.send(topic=topic, value=message, key=key.encode('utf-8')).add_callback(delivery_callback)

    # Wait for the message to be sent
    producer.flush()

    # Sleep for some time before generating the next message (e.g., 1 second)
    time.sleep(1)

