import csv
city=input("Enter a city: ").strip().lower()

with open("weather.csv","r") as file:
    data=list(csv.reader(file))
    for row in data[1:]:
        if row[0]==city:
            print(row[1])
