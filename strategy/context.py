from docs.strategy.strategy_imp import ConsoleOutput, KafkaOutput
from class_getter import get_config_class


class StrategyContext:
    def __init__(self):
        self.strategy_class = get_config_class()

    def exec_strategy(self):
        strategy_class = ConsoleOutput() if self.strategy_class.get_mode() == 'kafka' else KafkaOutput()
        while True:
            self.strategy_class.send_msg()
            print('New output mode detected:', strategy_class.get_mode())
            self.strategy_class, strategy_class = strategy_class, self.strategy_class
