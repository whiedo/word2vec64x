import pandas as pd
import datetime

path = "data/database/"
ending = "_DB.txt"

listOfFiles = ["FAI"] # , "FAM", "FAT"

for f in listOfFiles:
    print("start with file " + f)

    name = path + f + ending
    doc = open(name)
    with open(name) as file:
        lines = file.readlines()

        headers = []
        headersInit = False
        currentExcelRow = 1

        totalNoOfLines = len(lines)
        currentLine = 0

        #headers
        for i in range(0, totalNoOfLines):
            if (lines[i].rstrip() == "00F" and i + 2 < totalNoOfLines):
                buffer = lines[i + 2]
                buffer = buffer[2:]
                headers.append(buffer)
            elif (lines[i].rstrip() == "00I"):
                break

            currentLine += 1

        print("headers initialized.")

        csv_file = pd.DataFrame(headers)
        csv_file = csv_file.transpose()

        #lines
        for i in range(currentLine, totalNoOfLines):
            if (lines[i].rstrip() == "00I"):
                line_txt = []
                k = i + 1
                for j in range(k, k + len(headers)):
                    buffer = lines[j]
                    buffer = buffer[2:]
                    line_txt.append(buffer)
                csv_file.loc[currentExcelRow] = line_txt
                currentExcelRow += 1
                i = k + len(headers)

            currentLine += 1

            if (currentLine % 100000 == 0):
                print(str(datetime.datetime.now()) + " - percent completed: " + str(round(currentLine / totalNoOfLines, 3) * 100))

        writer = pd.ExcelWriter("data/database/excel/" + f + '_DB.xlsx')
        csv_file.to_excel(writer, 'Sheet1')
        writer.save()

        print("finished file " + f)