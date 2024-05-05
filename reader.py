import pandas as pd


def read_file():
    data = pd.read_csv('expenses_budget_vs_act.csv')
    return data
