import datetime
import fileinput

d = datetime.date.today()
'''book_date: 2015-07-28 00:00:00 +0000'''

today = d.strftime("%Y-%m-%d 00:00:00 +0000")
PATH = "../_config.yml"
# file = open(PATH,"r")
# for line in file.readlines():
#     if "book_date" in line:
#         print line
# file.close()

for line in fileinput.input(PATH, inplace=1):
    if "book_date" in line:
        line = "book_date: "+today
    line = line.replace("\n","")
    line = line.replace("\r","")
    print line


