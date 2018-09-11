import pandas as pd
from datetime import date
#Put respective lists in each column
col1 = pd.Series(data=['a1','b2','c1'])
col2 = pd.Series(data=['a1'])
col3 = pd.Series(data=['a1'])

#Put column name for respective lists here
col1.name = 'l1'
col2.name= 'l2'
col3.name= 'l3'

#df = pd.DataFrame(zip(col1,col2,col3), columns=[col1.name, col2.name,col3.name])
#df = pd.DataFrame.from_records([col1,col2,col3])- Row oriented
df = pd.concat([pd.DataFrame(col1),pd.DataFrame(col2), pd.DataFrame(col3)], axis=1) #column oriented    
#df.head()
df.to_csv("my_output1.csv")

create_date = "{:%m-%d-%y}".format(date.today())
created_by = "Ankit1"
footer = [('created_by',[created_by]),('created_on',[create_date]),('Version',[1.1])]
df_footer = pd.DataFrame.from_items(footer)
writer = pd.ExcelWriter('sample.xlsx',engine='xlsxwriter')
df.to_excel(writer,index = False)
df_footer.to_excel(writer, startrow = 6, index = False)
writer.save()
