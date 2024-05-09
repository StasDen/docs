from kafka import KafkaProducer, KafkaConsumer
from mode_getter import get_config_mode
from strategy_abs import MessageOutput
from docs.reader import read_file
from json import dumps, loads
from time import sleep


class ConsoleOutput(MessageOutput):
    def __init__(self):
        self.consumer = KafkaConsumer(
            'budget',
            bootstrap_servers=['localhost:9092'],
            group_id='budget',
            enable_auto_commit=True,
            value_deserializer=lambda m: loads(m.decode('utf-8'))
        )
        self.__mode = 'console'

    def get_mode(self):
        return self.__mode

    def send_msg(self):
        for msg in self.consumer:
            print('New record:\n', msg.value)
            sleep(3)
            if get_config_mode() != self.__mode:
                break


class KafkaOutput(MessageOutput):
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda m: dumps(m).encode('utf-8')
        )
        self.__mode = 'kafka'
        self.__rows_sent = 0

    def get_mode(self):
        return self.__mode

    def send_msg(self):
        data = read_file('../expenses_budget_vs_actual.csv', row_from=self.__rows_sent)
        col = data.columns.tolist()
        topic = 'budget'

        record = {}
        for row in data.values:
            i = 0
            for val in row:
                record[col[i]] = val
                i += 1

            self.producer.send(topic, record)
            self.__rows_sent += 1
            print(f'Message was sent to "{topic}" topic')
            sleep(2)
            if get_config_mode() != self.__mode:
                break
