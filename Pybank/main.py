import os
import csv

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)

    