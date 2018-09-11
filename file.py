fhand = open(input('enter the file name: '))
dummy = []
dummytins = []
# reading lines in the input file
for lines in fhand:
    if lines.startswith('N1*PE*'):
        dummy = lines.split('*')
        if dummy[3] == 'FI':
            dummytins.append(dummy[4].strip().split('~')[0])
    elif lines.startswith('REF*TJ*'):
        dummy = lines.split('*')
        dummytins.append(dummy[2].strip().split('~')[0])
print(dummytins)
