import csv

def read_csv_data(filepath):
    data = []
    with open("/Users/chiranth.c/Documents/selenium_framework/constants/data/saus_demo_login.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data
    