from collections import defaultdict
from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*")))
#we can add multiple file types as below
#root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
fhand = open(root.filename)
dcs = defaultdict(list) #contains the list of tins attached to the payer/subpayer
dct = defaultdict(list) #contains the list of tins attached to the 835 id
#if key is not find, it will be added to the dictionary
#dct['a'].append('b')
#dct['a'].append('c')
dummysubpayerId = [] #contins all the payer/subpayer id in the file
dummytins = [] # contains the list of tins
dummy = [] # is a variable, which contains split data of the line
dummy835Id = [] # contains the list of different 835 ids
for lines in fhand:
    if lines.startswith('TRN*'):
        dummy = []
        dummy  = lines.split('*')
        subid = dummy[3][1:]
        dummysubpayerId.append(subid)
        id_835 = dummy[4].split('~')[0][4:]
        dummy835Id.append(id_835)
    if lines.startswith('N1*PE*'):
        dummy = []
        dummy = lines.split('*')
        if dummy[3] == 'FI':
            tin = dummy[4].strip().split('~')[0]
            dummytins.append(tin)
            dcs[subid].append(tin)
            dct[id_835].append(tin)
    elif lines.startswith('REF*TJ*'):
        dummy = []
        dummy = lines.split('*')
        tin = dummy[2].strip().split('~')[0]
        dummytins.append(tin)
        dcs[subid].append(tin)
        dct[id_835].append(tin)
print(dcs,dummytins,dummy835Id,dct)
