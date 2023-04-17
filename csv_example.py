import csv
from datetime import datetime

path = "C:\\Users\\AapoJaakkola\\python\\data.csv"
file = open(path)
reader = csv.reader(file)

header = next(reader)

data = []
for row in reader:
    etunimi = row[1]
    sukunimi = row[2]
    ikä = int(row[3])
    päivä = datetime.strptime(row[4], '%m/%d/%Y')
    data.append([etunimi, sukunimi, ikä, päivä])
    
print(data[0])

return_path = "C:\\Users\\AapoJaakkola\\python\\modifieddata.csv"
file = open(return_path, 'w')
writer = csv.writer(file)
writer.writerow(["päivä", "nimi", "ikä"])
for i in range(len(data) - 1 ):
    row = data[i]
    formatted_date = row[3].strftime('%d.%m.%Y')
    writer.writerow([formatted_date, row[0] +" " +row[1], row[2]]) 
    



