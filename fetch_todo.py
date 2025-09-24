import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Berlin', 'Paris', 'London']
}

df = pd.DataFrame(data)
print(df)