from collections import defaultdict
from tkinter import filedialog
from tkinter import *
#below code is for opening the file dailog box to open the file, make sure your file is .txt
root = Tk()
root.withdraw()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
#print (root.filename)

dct = defaultdict(list)
#if key is not find, it will be added to the dictionary
#dct['a'].append('b')
#dct['a'].append('c')
#print(dct)
#fhand = open(input('enter the file name: '))
fhand = open(root.filename)
dummy_id = []
dummy835Id = []
dummytins = []
dummy = []
# reading lines in the input file
for lines in fhand:
    if lines.startswith('TRN*'):
        dummy_id = lines.split('*')
        id_835 = dummy_id[4].split('~')[0][3:]
        dummy835Id.append(id_835)
    if lines.startswith('N1*PE*'):
        dummy = lines.split('*')
        if dummy[3] == 'FI':
            tin = dummy[4].strip().split('~')[0]
            dummytins.append(tin)
            dct[id_835].append(tin)
    elif lines.startswith('REF*TJ*'):
        dummy = lines.split('*')
        tin = dummy[2].strip().split('~')[0]
        dummytins.append(tin)
        dct[id_835].append(tin)
print(dct)
