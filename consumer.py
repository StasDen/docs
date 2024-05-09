from kafka import KafkaConsumer
from time import sleep
from json import loads

consumer = KafkaConsumer(
    'budget',
    bootstrap_servers=['localhost:9092'],
    group_id='budget',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda m: loads(m.decode('utf-8'))
)

for rec in consumer:
    print('New record:\n', rec.value)
    sleep(3)
