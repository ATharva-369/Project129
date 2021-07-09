#This prorgram merges two csv files and stores it as a csv file
import csv
import pandas as pd

#creating a empty list to store data from the first csv file
firstcsv_data = []
#storing the data from the first csv file
with open('scrapper.csv') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        firstcsv_data.append(row)

#storing the headers and rows
headers = firstcsv_data[0]
firstcsv_rows = firstcsv_data[1:]

#creating a empty list to store data from the second csv file
secondcsv_data = []
#storing the data from the second csv file
with open('scrapper_valuechanged.csv') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        secondcsv_data.append(row)
#storing the rows
secondcsv_rows = secondcsv_data[1:]

#merging the rows and removing the first unecessary element
firstcsv_rows.extend(secondcsv_rows)
firstcsv_rows.pop(0)

#saving the merged data into a csv file
with open("merged.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(firstcsv_rows)

