import os
import pandas as pd
arr = os.listdir()
col1 = pd.Series(data=arr)
#Put column name for respective lists here
col1.name = 'l1'
df = pd.DataFrame(col1)
df.to_csv("my_output1.csv")
