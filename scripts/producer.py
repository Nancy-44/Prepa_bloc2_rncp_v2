from kafka import KafkaProducer
import json

producer=KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

producer.send("users_json", {"user_id":1,"event":"click"})
producer.flush()
producer.close()