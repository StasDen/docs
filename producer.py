from kafka import KafkaProducer
from reader import read_file
from time import sleep
from json import dumps

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda m: dumps(m).encode('utf-8')
)

file_end = False
while not file_end:
    data = read_file()
    col = data.columns.tolist()
    topic = 'budget'
    report = {}

    for row in data.values:
        i = 0
        for val in row:
            report[col[i]] = val
            i += 1

        producer.send(topic, report)
        print(f'Message has been sent to "{topic}" topic')
        sleep(2)
    file_end = True
