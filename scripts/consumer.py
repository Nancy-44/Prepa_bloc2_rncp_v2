from kafka import KafkaConsumer
import json
consumer = KafkaConsumer(
    'users_json',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    consumer_timeout_ms=5000  # 5 secondes max si pas de message
)
for message in consumer:
    print(f"Received message: {message.value}")