from strategy_imp import ConsoleOutput, KafkaOutput
from typing import Union
from json import loads


def get_config_class() -> Union[ConsoleOutput, KafkaOutput]:
    try:
        f = open('config.json')
        data_dict = loads(f.read())
        strategy_class = ConsoleOutput() if data_dict['consoleOutput'] else KafkaOutput()
        return strategy_class
    except FileNotFoundError:
        print('Error: specified file was not found')
    except Exception as e:
        print('Error occurred:\n', e)
