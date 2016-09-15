import pandas as pd

def test_run():
    df = pd.read_csv("http://chart.finance.yahoo.com/table.csv?s=GE&a=7&b=14&c=2016&d=8&e=14&f=2016&g=d&ignore=.csv")
    print df
if __name__ == "__main__":
    test_run()
