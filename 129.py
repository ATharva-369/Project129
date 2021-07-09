#This program will clean and sort the data we have obtained from webscrapping the wikipedia page
import csv 
import pandas as pd

#opening the obtained csv file
data =[]
with open("scrapper_final.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)
   

headers = data[0][1:] #setting the headers
brown_stars_data = data[1:] #setting the rows

#removing the unnecessary first indexing column and appending all of the data into a list
stars_data = []
for i in brown_stars_data:
    i.pop(0)
    stars_data.append(i) 

#converting the data into lowercase
for data_point in stars_data:
    data_point[1] = data_point[1].lower()

#sorting the data
stars_data.sort(key=lambda stars_data: stars_data[1])

#storing the data as a sorted csv
with open("scrapper_sorted.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)

#opening and reading the sorted csv
df = pd.read_csv('scrapper_sorted.csv')
del df[df.columns[0]] # deleting the unncessary the column
new_df = df.dropna() #dropping all the empty values
new_df.to_csv("scrapper_cleaned.csv") #saving the data into cleaned.csv

cleaned_data = [] #creating a cleaned list to append data to 
#opening the cleaned csv and appending the data into our list
with open("scrapper_cleaned.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        cleaned_data.append(row)

#storing the headers and rows seperately        
cleaned_headers = cleaned_data[0][1:]
cleaned_stars = cleaned_data[1:]

#creating a list to store data without the unnecessary column
cleaned_final_data = []

#removing the unecessary column
for i in cleaned_stars:
    i.pop(0)
    
    cleaned_final_data.append(i)


#converting the radius and mass into solar radius and solar mass
for i in cleaned_final_data:
    i[3]= float(i[3])*0.102763
    i[2] =float(i[2])*0.000954588

#storing the final data into a csv file
with open("scrapper_valuechanged.csv", "w+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(cleaned_headers)
    csvwriter.writerows(cleaned_final_data)

# print(cleaned_final_data[0])