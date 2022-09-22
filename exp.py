import json
import pandas as pd

df = json.load(open('result.json'))

print(pd.DataFrame(df["8R"]))
#print(df)