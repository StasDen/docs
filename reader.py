import pandas as pd


def read_file(name, row_from=0):
    try:
        return pd.read_csv(name, skiprows=row_from)
    except FileNotFoundError:
        print('Error: specified file was not found')
    except pd.errors.ParserError as e:
        print('Error occurred when parsing csv:\n', e)
    except Exception as e:
        print('Error occurred:', e)
