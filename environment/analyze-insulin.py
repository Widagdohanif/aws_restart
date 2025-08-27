import re

data = ""

with open("preproinsulin-seq.txt", "r") as data_insulin:
    for i in data_insulin:
        if i.islower():
            data += re.sub(r'[0-9\s]+', '', i)

with open('preproinsulin-seq-clean.txt', "w") as pi:
    pi.write(data)

with open("lsinsulin-seq-clean.txt", "w") as li:
    li.write(data[0:24])

with open("binsulin-seq-clean.txt", "w") as li:
    li.write(data[24:54])
    
with open("cinsulin-seq-clean.txt", "w") as li:
    li.write(data[54:89])
    
with open("ainsulin-seq-clean.txt", "w") as li:
    li.write(data[89:110])