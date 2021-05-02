#readfile
'''f = open("filetoread.txt", "w")
f.write("127 122")
f.close()'''

f = open("filetoread.txt", "r")
#print(f.read())
newstring = f.read()
f.close()

data_CCS = newstring.split(" ")#separe les valeurs du CO2 et de TOVC
intedata = int(data_CCS[0])
intedata = intedata -100
print(intedata)
print(data_CCS[1])

d1 = 300
d2 = 457
f = open("filetoread.txt", "w")
f.write(str(d1) +" "+str(d2))
f.close()
