import os
import csv

os.chdir(os.path.dirname(__file__))
PyBankcsv = os.path.join("Data","budget_data.csv")

month = []
profit = []
profit_delta = []

with open(PyBankcsv, 'r') as csvfile:
    csvread = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvread)

    for row in csvread:
        month.append(row[0])
        profit.append(int(row[1]))
     
    for i in range(len(profit)-1):
        profit_delta.append(profit[i+1]-profit[i])

increase = max(profit_delta)
decrease = min(profit_delta)

month_increase = profit_delta.index(max(profit_delta))+1
month_decrease = profit_delta.index(min(profit_delta))+1

Analysistxt = os.path.join("Analysis","financial_analysis_txt")

with open(Analysistxt, 'w') as text:
    text.write('Financial Analysis\n')
    text.write('----------------------------\n')
    text.write(f"Total Months:{len(month)} \n")
    text.write(f"Total: ${sum(profit)} \n")
    text.write(f"Average Change: ${round(sum(profit_delta)/len(profit_delta),2)} \n")
    text.write(f"Greatest Profit Increase: {month[month_increase]} (${(str(increase))}) \n")
    text.write(f"Greatest Profit Decrease: {month[month_decrease]} (${(str(decrease))})")

with open(Analysistxt, 'r') as readfile:
    print(readfile.read())