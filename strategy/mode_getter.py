from json import loads


def get_config_mode():
    try:
        f = open('config.json')
        data_dict = loads(f.read())
        mode = 'console' if data_dict['consoleOutput'] else 'kafka'
        return mode
    except FileNotFoundError:
        print('Error: specified file was not found')
    except Exception as e:
        print('Error occurred:', e)
