import pandas as pd

df = pd.read_excel("sales_transactions.xlsx")
print(df.groupby('order')["ext price"].sum())
order_total = df.groupby('order')["ext price"].sum().rename("Order_Total").reset_index()
print(order_total)
df_1 = df.merge(order_total)
df_1["Percent_of_Order"] = df_1["ext price"] / df_1["Order_Total"]
df["OrderTotal"] = df.groupby('order')["ext price"].transform('sum')
df["PercentofOrder"] = df["ext price"] / df["OrderTotal"]
print(df)
print (df_1)
