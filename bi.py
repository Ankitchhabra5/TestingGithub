import csv
import pandas as pd
from collections import defaultdict
from tkinter import filedialog
from tkinter import *
from decimal import *

root = Tk()
root.withdraw()
root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
# we can add multiple file types as below
# root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
fhand = open(root.filename)
dcs = defaultdict(list)  # contains the list of tins attached to the payer/subpayer
dct = defaultdict(list)  # contains the list of tins attached to the 835 id
dcid = defaultdict(list)  # contains the list of subpayers attached to the 835 id
dcbpr = defaultdict(Decimal)  # contains the sum of each 835 ids
# if key is not find, it will be added to the dictionary
# dct['a'].append('b')
# dct['a'].append('c')
dummysubpayerId = []  # contins all the payer/subpayer id in the file
dummytins = []  # contains the list of tins
dummy = []  # is a variable, which contains split data of the line
dummy835Id = []  # contains all the 835 ids
count_bpr = 0
count_ev = 0
count_2u = 0

csv = open("a1.csv", "a")
columnTitleRow = "tin,payment number, payerid, payer/subpayertin \n"
sv.write(columnTitleRow)

'''for key in dic.keys():
	name = key
	email = dic[key]
	row = name + "," + email + "\n"
	csv.write(row)
'''

for lines in fhand:
    if lines.startswith('BPR*'):
        count_bpr = count_bpr + 1
        bpr_amount = Decimal(lines.split('*')[2])

    if lines.startswith('REF*EV*'):
        count_ev = count_ev + 1
    if lines.startswith('REF*2U*'):
        count_2u = count_2u + 1

    if lines.startswith('TRN*'):

        dummy = []
        dummy = lines.split('*')
        payment_number = str(dummy[2])
        print(payment_number)
        subid = dummy[3]
        dummysubpayerId.append(subid)  # adding subpayer payer to the list
        id_835 = "'" + str(dummy[4].split('~')[0][4:])
        dummy835Id.append(id_835)  # adding 835ids to the list
        if id_835 in dcid.keys():  # this code will check if 835 id is already present or not
            if subid not in dcid[id_835]:
                # if subpayer/payer is already associated with the 835 id, it will not apppend else it will do
                dcid[id_835].append(subid)
            dcbpr[id_835] = dcbpr[id_835] + bpr_amount

        else:
            dcid[id_835].append(
                subid)  # create a new key for the 835 id if not present and add the subpayer/payer tin to it
            dcbpr[id_835] = bpr_amount

            # Tin can be found in N1 segment or Ref TJ segment, first we are validating the N1 level then Ref level

    if lines.startswith('N1*PE*'):
        dummy = []
        dummy = lines.split('*')
        if dummy[3] == 'FI':
            tin = str(dummy[4].strip().split('~')[0])
            dummytins.append(tin)  # adding tins to the list
            # below code will check whether subpyaer/payer already as key is present in DCS or not
            # After that if it is present, then it will check whether tin is associated with that payer/subpayer or not
            # if not it will add the tin to it
            # and if in starting if subpayer/payer id is not present in keys, it will add it to the keys
            row = "'" + str(tin) + "," + "'" + str(payment_number) + "," + "'" + str(id_835) + "," + "'" + str(
                subid) + "\n"
            csv.write(row)
            if subid in dcs.keys():
                if tin not in dcs[subid]:
                    dcs[subid].append(tin)
            else:
                dcs[subid].append(tin)
            # below code will check whether 835 id as key is present in DCT or not
            # After that if it is present, then it will check whether tin is associated with that 835 id or not
            # if not it will add the tin to it
            # and if in starting if 835 id is not present in keys, it will add it to the keys
            if id_835 in dct.keys():
                if tin not in dct[id_835]:
                    dct[id_835].append(tin)
            else:
                dct[id_835].append(tin)

    elif lines.startswith('REF*TJ*'):
        dummy = []
        dummy = lines.split('*')
        tin = str(dummy[2].strip().split('~')[0])
        row = "'" + str(tin) + "," + "'" + str(payment_number) + "," + "'" + str(id_835) + "," + "'" + str(subid) + "\n"
        csv.write(row)
        dummytins.append(tin)  # adding tins to the list
        # below code will check whether subpyaer/payer already as key is present in DCS or not
        # After that if it is present, then it will check whether tin is associated with that payer/subpayer or not
        # if not it will add the tin to it
        # and if in starting if subpayer/payer id is not present in keys, it will add it to the keys
        if subid in dcs.keys():
            if tin not in dcs[subid]:
                dcs[subid].append(tin)
        else:
            dcs[subid].append(tin)
        # below code will check whether 835 id as key is present in DCT or not
        # After that if it is present, then it will check whether tin is associated with that 835 id or not
        # if not it will add the tin to it
        # and if in starting if 835 id is not present in keys, it will add it to the keys
        if id_835 in dct.keys():
            if tin not in dct[id_835]:
                dct[id_835].append(tin)
        else:
            dct[id_835].append(tin)
# printing dictionaries
# print('#contains the list of tins attached to the payer/subpayer',dcs)
# print('#contains all the 835 ids sum',dcbpr)
# print('#contains the list of tins attached to the 835 id',dct)
# print('#contains the list of subpayers attached to the 835 id',dcid)
# print('#contins all the payer/subpayer id in the file',dummysubpayerId)
count_tins = len(dummytins)  # count the number of tins in the file
count_835ids = len(dummy835Id)  # Count the number of times 835 id is there
count_sub_payerid = len(dummysubpayerId)  # count the number of times payer /subpayer tins
actual_tins = []  # list of unoque tins
actual_835ids = []  # list of unique 835 ids
actual_sub_payerid = []  # list of unique payer/subpayer id

# Below is the code to make the above lists to have unique tins
for i in dummy835Id:
    if i not in actual_835ids:
        actual_835ids.append(i)
for i in dummysubpayerId:
    if i not in actual_sub_payerid:
        actual_sub_payerid.append(i)
for i in dummytins:
    if i not in actual_tins:
        actual_tins.append(i)


# print('# contains the list of tins',actual_tins)
# print('#contains all the 835 ids',actual_835ids)
# print('#contins all the payer/subpayer id in the file',actual_sub_payerid)
# print('count_tins',count_tins)
# print('count_835ids',count_835ids)
# print('count_sub_payerid',count_sub_payerid)
# print('count_2u',count_2u)
# print('count_bpr',count_bpr)
# print('count_ev',count_ev)
csv.close()
# Put respective lists in each column
col1 = pd.Series(data=actual_tins)
col2 = pd.Series(data=actual_835ids)
col3 = pd.Series(data=actual_sub_payerid)
col4 = pd.Series(data=count_tins)
col5 = pd.Series(data=count_835ids)
col6 = pd.Series(data=count_sub_payerid)
col7 = pd.Series(data=count_2u)
col8 = pd.Series(data=count_bpr)
col9 = pd.Series(data=count_ev)
col10 = pd.Series(data=['Tins attached to the subpayer'])
col11 = pd.Series(data=['BPR Amount', 'Tins attahed to the 835 IDs', 'Subpayer/payer id associated to the 835ids'])
# Put column name for respective lists here
col1.name = 'actual_tins'
col2.name = 'actual_835ids'
col3.name = 'actual_sub_payerid'
col4.name = 'count_tins'
col5.name = 'count_835ids'
col6.name = 'count_sub_payerid'
col7.name = 'count_2u'
col8.name = 'count_bpr'
col9.name = 'count_ev'
col10.name = 'Payer/subpayerid'
col11.name = '835 IDs'
# df = pd.DataFrame(zip(col1,col2,col3), columns=[col1.name, col2.name,col3.name])
df = pd.concat([pd.DataFrame(col1), pd.DataFrame(col2), pd.DataFrame(col3), pd.DataFrame(col4), pd.DataFrame(col5),
                pd.DataFrame(col6), pd.DataFrame(col7), pd.DataFrame(col8), pd.DataFrame(col9), pd.DataFrame(col10),
                pd.DataFrame([dcs]), pd.DataFrame(col11), pd.DataFrame([dcbpr, dct, dcid])], axis=1)
# df.head()
df.to_csv("my_output.csv")

# pd.DataFrame(dcs) , pd.DataFrame(dcbpr), pd.DataFrame(dct), pd.DataFrame(dcid),


# print('#contains the list of tins attached to the payer/subpayer',dcs)
# print('#contains all the 835 ids sum',dcbpr)
# print('#contains the list of tins attached to the 835 id',dct)
# print('#contains the list of subpayers attached to the 835 id',dcid)
