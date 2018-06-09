# -*- coding: utf-8 -*-
import unicodedata
import re
import binascii

print("create protyp array")

name = "data/database/PROTYP.txt"

prototypeArray = [[0 for j in range(2)] for i in range(181)]

with open(name) as file:
    lines = file.readlines()

    headers = []
    headersInit = False
    currentExcelRow = 1

    totalNoOfLines = len(lines)
    currentLine = 0

    # headers
    for i in range(0, totalNoOfLines):
        if (lines[i].rstrip() == "00F" and i + 2 < totalNoOfLines):
            buffer = lines[i + 2]
            buffer = buffer[2:]
            headers.append(buffer)
        elif (lines[i].rstrip() == "00I"):
            break

        currentLine += 1

    # lines
    rowCounter = 0
    for i in range(currentLine, totalNoOfLines):
        if (lines[i].rstrip() == "00I"):
            k = i + 1
            columCounter = 1
            for j in range(k, k + len(headers)):
                buffer = lines[j]
                buffer = buffer[2:]
                if (columCounter == 1):
                   prototypeArray[rowCounter][0] = buffer
                if (columCounter == 5):
                    prototypeArray[rowCounter][1] = buffer
                columCounter += 1
            currentExcelRow += 1
            i = k + len(headers)

            rowCounter += 1

        currentLine += 1





path = "data/database/"
filename = "merged_DB.txt"
newFilename = "merged_placeholder_DB.txt"

print("start with replacing placeholders")

doc = open(path + filename,'r')
input = doc.read()
doc.close()

input = input.replace("~b", " ")
input = input.replace("~c", "")
input = input.replace("~d", "")
input = input.replace("~f", "")
input = input.replace("~g", " ")
input = input.replace("~h", "")
input = input.replace("~i", "    ")  # tab
input = input.replace("~k", "")
input = input.replace("~n", " ")  # return
input = input.replace("~t", "")
input = input.replace("~u", "")
input = input.replace("~w", "")

for i in range(len(prototypeArray)):
    ##[i][1] = unicode
    # #[i][0] = placeholder
    s = prototypeArray[i][1]
    s = s.replace('\n','')
    placeholder = '\\' + prototypeArray[i][0].replace('\n', '')
    placeholder = u'' + placeholder

    print(s)
    print(placeholder)

    cp2chr = lambda c: (b'\\u' + c.encode('ascii')).decode('raw_unicode_escape')
    #cp2chr = lambda c: binascii.unhexlify(c.zfill(len(c) + (len(c) & 1))).decode('utf-8')
    newS = cp2chr(s)

    print(newS)

    #if (s == '2265') or (s == '03BC') or (s == '03B3') or (s == '03B1') or (s == '03B2') or (s == '2264') or \
     #       (s == '2033') or (s == '2032'):
      #  newS = ''

    input = input.replace(placeholder,newS)

outputFile = open(path + newFilename,'w', encoding='utf-8')
outputFile.write(input)
#with open(path  + newFilename, 'w', encoding='utf-8') as f: f.write(input)
outputFile.close()

print("finished placeholders.")