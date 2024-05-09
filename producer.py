from kafka import KafkaProducer
from reader import read_file
from time import sleep
from json import dumps

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda m: dumps(m).encode('utf-8')
)

while True:
    data = read_file('expenses_budget_vs_actual.csv')
    col = data.columns.tolist()
    topic = 'budget'

    report = {}
    for row in data.values:
        i = 0
        for val in row:
            report[col[i]] = val
            i += 1

        producer.send(topic, report)
        print(f'Message was sent to "{topic}" topic')
        sleep(2)
