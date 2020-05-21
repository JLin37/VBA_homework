import os
import csv

udemy_csv = "lotto_numbers.csv"

first = '3957481'
second = '5865187'
third = '2817729'

Runner_up1 = '2275339'
Runner_up2 = '5868182'
Runner_up3 = '1841402'

Winners = {}

# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(udemy_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        lotto_num = row[2]
        first_name = row[0]
        last_name = row[1]
        
        if first == lotto_num:
            Winners["First Place Winner"] = [first_name, last_name, lotto_num]
        elif second == lotto_num:
            Winners["Second Place Winner"] = [first_name, last_name, lotto_num]
        elif third == lotto_num:
            Winners["Third Place Winner"] = [first_name, last_name, lotto_num]  
        elif Runner_up1 == lotto_num or Runner_up2 == lotto_num or Runner_up3 == lotto_num:
            if "Runner Up" not in Winners:
                Winners["Runner Up"] = [first_name, last_name, lotto_num]

for key, value in Winners.items():
    print(f"{key} is {value[0]} {value[1]} and his winning number is {value[2]}")
        