import numpy
import pandas as pd

datafile =open("data.pgxseg")

for i in range(1006):
    datafile.readline()

names = datafile.readline().split()
linelist=[]

while True:
    line=datafile.readline()
    linelist.append(line.split())
    if line == "":
        break


print(pd.DataFrame(data=linelist, columns=names))


datafile.close()
