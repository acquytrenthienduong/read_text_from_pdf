from PyPDF2 import PdfReader
import xlsxwriter
import glob
import re

workbook = xlsxwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet()

number = 0
number1 = 0

for file in glob.glob("data/*.pdf"):
    print(file)
    reader = PdfReader(file)
    for x in range(len(reader.pages)):
        page = reader.pages[x]
        text = page.extract_text()
        print(text)
        array = text.split()
        for i in array:
            raw = re.sub('[^A-Za-z0-9]+', "", i)
            # print(raw)
            if('@' in i):
                value = i.replace("", "")
                worksheet.write(number , 0 , value.replace("", ""))

            if((raw.isnumeric() and len(raw) >= 8 and raw.startswith("0")) or "+84" in raw):
                phoneNumber = raw
                # print(i)
                # print(phoneNumber)
                if(len(raw) <= 8): value = "+84" + raw
                worksheet.write(number1 , 1 , phoneNumber)
    print("=====================>")
    number += 1
    number1 += 1
workbook.close()
